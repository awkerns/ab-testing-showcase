"""
Bayesian Analysis Module
========================

Bayesian A/B testing using Beta-Binomial conjugate prior model.
Calculates posterior distributions, probability that B is better than A,
and credible intervals.
"""

import pandas as pd
import numpy as np
from scipy.stats import beta
from typing import Dict, Any


def run_bayesian_test(
    data: pd.DataFrame,
    prior_alpha: float = 1.0,
    prior_beta: float = 1.0,
    n_samples: int = 100000,
    return_samples: bool = False,
) -> Dict[str, Any]:
    """
    Perform Bayesian A/B test using Beta-Binomial model.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame with 'group' and 'converted' columns
    prior_alpha : float
        Alpha parameter for Beta prior (default = 1 for uniform)
    prior_beta : float
        Beta parameter for Beta prior (default = 1 for uniform)
    n_samples : int
        Number of posterior samples to draw
    return_samples : bool
        Whether to return raw posterior samples (needed for plotting)

    Returns
    -------
    Dict[str, Any]
        Dictionary containing Bayesian analysis results
    """
    # Split data
    group_a = data[data["group"] == "A"]
    group_b = data[data["group"] == "B"]

    successes_a = group_a["converted"].sum()
    n_a = len(group_a)
    successes_b = group_b["converted"].sum()
    n_b = len(group_b)

    # Posterior parameters (conjugate update)
    post_alpha_a = prior_alpha + successes_a
    post_beta_a = prior_beta + n_a - successes_a
    post_alpha_b = prior_alpha + successes_b
    post_beta_b = prior_beta + n_b - successes_b

    # Draw samples from posterior
    samples_a = beta.rvs(post_alpha_a, post_beta_a, size=n_samples)
    samples_b = beta.rvs(post_alpha_b, post_beta_b, size=n_samples)

    # Calculate key metrics
    mean_a = post_alpha_a / (post_alpha_a + post_beta_a)
    mean_b = post_alpha_b / (post_alpha_b + post_beta_b)
    
    uplift_pct_bayes = ((mean_b - mean_a) / mean_a * 100) if mean_a > 0 else 0.0
    prob_b_better = np.mean(samples_b > samples_a)

    # 95% Credible Intervals
    ci_a = beta.ppf([0.025, 0.975], post_alpha_a, post_beta_a)
    ci_b = beta.ppf([0.025, 0.975], post_alpha_b, post_beta_b)

    results: Dict[str, Any] = {
        "mean_conversion_a": mean_a,
        "mean_conversion_b": mean_b,
        "uplift_pct_bayes": uplift_pct_bayes,
        "prob_b_better": prob_b_better,
        "credible_interval_a": ci_a.tolist(),
        "credible_interval_b": ci_b.tolist(),
        "bayesian_significant": prob_b_better > 0.95,
    }

    if return_samples:
        results["samples_a"] = samples_a
        results["samples_b"] = samples_b

    return results
