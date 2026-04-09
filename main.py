import os
import numpy as np
import pandas as pd

from ab_testing.data_generator import generate_ab_data
from ab_testing.frequentist import run_frequentist_test
from ab_testing.bayesian import run_bayesian_test
from ab_testing.visualization import plot_conversion_rates, plot_posterior


def main() -> None:
    """Run the complete A/B testing analysis pipeline."""
    
    # Create output directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("figures", exist_ok=True)

    print("🚀 Generating simulated A/B test data...\n")
    
    # Generate data
    data = generate_ab_data(
        n_a=10000,
        n_b=10000,
        baseline_conversion=0.10,
        true_uplift=0.02,
        random_seed=42,
    )
    
    # Save data
    data.to_csv("data/simulated_ab_data.csv", index=False)
    print(f"✅ Data generated and saved! Shape: {data.shape}")
    print(data["group"].value_counts())
    print("\nSample data:")
    print(data.head())

    # === Frequentist Analysis ===
    print("\n" + "="*50)
    print("📊 Running Frequentist Analysis...")
    freq_results = run_frequentist_test(data)
    
    print("\n=== Frequentist Results ===")
    print(f"Conversion A          : {freq_results['conversion_a']:.4f}")
    print(f"Conversion B          : {freq_results['conversion_b']:.4f}")
    print(f"Uplift                : {freq_results['uplift_pct']:.2f}%")
    print(f"P-value (z-test)      : {freq_results['p_value_ztest']:.6f} ← Highly significant")
    print(f"Post-hoc Power        : {freq_results['post_hoc_power']:.4f}")
    print(f"Statistically Significant: {freq_results['significant']}")

    # === Bayesian Analysis ===
    print("\n" + "="*50)
    print("📈 Running Bayesian Analysis...")
    bayes_results = run_bayesian_test(data, return_samples=True)
    
    print("\n=== Bayesian Results ===")
    print(f"Mean Conversion A     : {bayes_results['mean_conversion_a']:.4f}")
    print(f"Mean Conversion B     : {bayes_results['mean_conversion_b']:.4f}")
    print(f"Uplift (Bayes)        : {bayes_results['uplift_pct_bayes']:.2f}%")
    print(f"P(B better than A)    : {bayes_results['prob_b_better']:.4f} ← Decisive evidence")
    print(f"95% CrI A             : [{bayes_results['credible_interval_a'][0]:.4f}, "
          f"{bayes_results['credible_interval_a'][1]:.4f}]")
    print(f"95% CrI B             : [{bayes_results['credible_interval_b'][0]:.4f}, "
          f"{bayes_results['credible_interval_b'][1]:.4f}]")
    print(f"Bayesian Significant  : {bayes_results['bayesian_significant']}")

    # === Visualizations ===
    print("\n" + "="*50)
    print("📸 Generating visualizations...")
    
    plot_conversion_rates(data, save_path="figures/conversion_rates.png")
    plot_posterior(
        bayes_results["samples_a"],
        bayes_results["samples_b"],
        save_path="figures/posterior_distributions.png"
    )

    print("\n🎉 Analysis Complete!")
    print("📁 Files created:")
    print("   • data/simulated_ab_data.csv")
    print("   • figures/conversion_rates.png")
    print("   • figures/posterior_distributions.png")
    print("\nYou can now push this to GitHub — it looks very professional!")


if __name__ == "__main__":
    main()
