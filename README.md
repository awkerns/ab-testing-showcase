# ab-testing-showcase

**A clean, production-ready Python project demonstrating professional A/B testing skills.**

Comprehensive analysis of simulated A/B test data using both **frequentist** (z-test, chi-square, post-hoc power) and **Bayesian** (Beta-Binomial conjugate model with Monte Carlo inference) approaches. Includes reproducible data generation, statistical testing, uplift calculation, visualizations, and clear interpretation.


---

## Features
- Simulated binary outcome data (e.g., conversion rates) with known ground-truth uplift
- Frequentist hypothesis testing + post-hoc power analysis
- Bayesian inference with posterior probabilities and credible intervals
- Publication-quality visualizations (automatically saved)
- Fully reproducible with fixed random seed
- Modular, well-documented, and type-hinted code
- Zero external data required — runs out of the box

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/ab-testing-showcase.git
cd ab-testing-showcase

# Install dependencies
pip install -r requirements.txt

# Run the full analysis
python main.py
```
Output: Console summary + data/ and figures/ folders with all results and plots.

## Methodology
### Data Generation
Control (A): 10% baseline conversion rate
Treatment (B): 12% conversion rate (+2% absolute uplift)
Sample size: 10,000 per group

### Frequentist Analysis
Two-proportion z-test
Chi-square test of independence
Post-hoc statistical power calculation

### Bayesian Analysis
Beta-Binomial model with uniform priors
Posterior sampling (100,000 draws)
Probability that B is better than A
95% credible intervals

### Visualizations
Conversion rate bar plot with 95% confidence intervals
Posterior distribution density plots


## Example Results
### Frequentist Results:
   • Conversion A: 0.0998
   • Conversion B: 0.1203
   • Uplift: 20.54%
   • P-value (z-test): 0.0000     ← Highly significant
   • Post-hoc Power: 0.9998

### Bayesian Results:
   • Mean Conversion A: 0.1000
   • Mean Conversion B: 0.1202
   • Uplift (Bayes): 20.20%
   • P(B better than A): 1.0000   ← Decisive evidence
   • 95% CrI A: [0.0943, 0.1058]
   • 95% CrI B: [0.1139, 0.1266]

Plots are saved in the figures/ folder at high resolution (300 DPI).

## Installation
Python 3.10+
Dependencies listed in requirements.txt

## Usage
You can easily modify test parameters in main.py:
Pythondata = generate_ab_data(
    n_a=20000,
    n_b=20000,
    baseline_conversion=0.15,
    true_uplift=0.03,
    random_seed=123
)

## Contributing
Feel free to open issues or submit pull requests for new features (e.g., sequential testing, multi-variant tests, CUPED, continuous metrics, etc.).

Made with ❤️ to showcase strong A/B testing and statistical analysis skills.
