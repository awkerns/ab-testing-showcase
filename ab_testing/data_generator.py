"""
Data Generator for A/B Testing
==============================

Generates synthetic binary outcome data (e.g., conversion) with known ground truth uplift.
Fully reproducible with random seed.
"""

import numpy as np
import pandas as pd
from typing import Optional


def generate_ab_data(
    n_a: int = 10000,
    n_b: int = 10000,
    baseline_conversion: float = 0.10,
    true_uplift: float = 0.02,
    random_seed: Optional[int] = 42,
) -> pd.DataFrame:
    """
    Generate simulated A/B test data with binary outcomes.

    Parameters
    ----------
    n_a : int
        Sample size for Control group (A)
    n_b : int
        Sample size for Treatment group (B)
    baseline_conversion : float
        True conversion rate for Control (A)
    true_uplift : float
        Absolute uplift for Treatment (B). Example: 0.02 = +2%
    random_seed : Optional[int]
        Random seed for full reproducibility

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: ['group', 'converted']
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate conversions (Bernoulli trials)
    conversions_a = np.random.binomial(n=1, p=baseline_conversion, size=n_a)
    conversions_b = np.random.binomial(
        n=1, 
        p=baseline_conversion + true_uplift, 
        size=n_b
    )

    # Create DataFrame
    df = pd.DataFrame({
        "group": ["A"] * n_a + ["B"] * n_b,
        "converted": np.concatenate([conversions_a, conversions_b])
    })

    return df
