"""
Frequentist Analysis Module
===========================

Performs classical statistical tests for A/B testing:
- Two-proportion z-test
- Chi-square test
- Post-hoc statistical power
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest, proportion_effectsize
from statsmodels.stats.power import zt_ind_solve_power
from typing import Dict


def run_frequentist_test(data: pd.DataFrame) -> Dict[str, float]:
    """
    Perform frequentist A/B testing analysis.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing 'group' and 'converted' columns

    Returns
    -------
    Dict[str, float]
        Dictionary with all key statistical results
    """
    # Split data by group
    group_a = data[data["group"] == "A"]["converted"]
    group_b = data[data["group"] == "B"]["converted"]

    n_a, n_b = len(group_a), len(group_b)
    conv_a = group_a.mean()
    conv_b = group_b.mean()

    # Chi-square test
    contingency = pd.crosstab(data["group"], data["converted"])
    chi2_stat, p_chi2, _, _ = chi2_contingency(contingency)

    # Two-proportion z-test
    counts = [group_a.sum(), group_b.sum()]
    nobs = [n_a, n_b]
    z_stat, p_z = proportions_ztest(counts, nobs, alternative="two-sided")

    # Relative uplift percentage
    uplift_pct = ((conv_b - conv_a) / conv_a * 100) if conv_a > 0 else 0.0

    # Post-hoc power calculation
    effect_size = proportion_effectsize(conv_a, conv_b)
    try:
        power = zt_ind_solve_power(
            effect_size=effect_size,
            nobs1=n_a,
            alpha=0.05,
            ratio=n_b / n_a,
            alternative="two-sided"
        )
    except:
        power = np.nan

    return {
        "conversion_a": conv_a,
        "conversion_b": conv_b,
        "uplift_pct": uplift_pct,
        "p_value_ztest": p_z,
        "p_value_chi2": p_chi2,
        "z_statistic": z_stat,
        "chi2_statistic": chi2_stat,
        "post_hoc_power": power,
        "significant": p_z < 0.05,
    }
