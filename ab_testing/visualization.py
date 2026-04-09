"""
Visualization Module
====================

Creates publication-quality plots for A/B test results:
- Conversion rate bar plot with confidence intervals
- Posterior distribution density plots
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional


def plot_conversion_rates(
    data: pd.DataFrame, 
    save_path: Optional[str] = "figures/conversion_rates.png"
) -> None:
    """
    Plot conversion rates by group with 95% confidence intervals.
    
    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing 'group' and 'converted' columns
    save_path : Optional[str]
        Path to save the figure (set to None to disable saving)
    """
    plt.figure(figsize=(8, 5))
    
    sns.barplot(
        x="group",
        y="converted",
        data=data,
        estimator=np.mean,
        errorbar=("ci", 95),
        capsize=0.15,
        palette=["#1f77b4", "#ff7f0e"],
        width=0.6
    )
    
    plt.title("Conversion Rates by Group\n(with 95% Confidence Intervals)", 
              fontsize=14, pad=20)
    plt.ylabel("Conversion Rate", fontsize=12)
    plt.xlabel("Group", fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, group in enumerate(['A', 'B']):
        mean = data[data['group'] == group]['converted'].mean()
        plt.text(i, mean + 0.005, f"{mean:.4f}", 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"   ✅ Saved: {save_path}")
    
    plt.close()


def plot_posterior(
    samples_a: np.ndarray,
    samples_b: np.ndarray,
    save_path: Optional[str] = "figures/posterior_distributions.png"
) -> None:
    """
    Plot posterior distributions for both groups.
    
    Parameters
    ----------
    samples_a : np.ndarray
        Posterior samples for Group A
    samples_b : np.ndarray
        Posterior samples for Group B
    save_path : Optional[str]
        Path to save the figure
    """
    plt.figure(figsize=(10, 6))
    
    sns.kdeplot(
        samples_a, 
        label="Group A (Control)",
        fill=True,
        alpha=0.6,
        color="#1f77b4",
        linewidth=2
    )
    sns.kdeplot(
        samples_b, 
        label="Group B (Treatment)",
        fill=True,
        alpha=0.6,
        color="#ff7f0e",
        linewidth=2
    )
    
    plt.title("Posterior Distributions of Conversion Rates", 
              fontsize=14, pad=20)
    plt.xlabel("Conversion Rate", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.legend(title="Group", fontsize=11)
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"   ✅ Saved: {save_path}")
    
    plt.close()
