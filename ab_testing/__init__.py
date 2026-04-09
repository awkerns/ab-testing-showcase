"""
A/B Testing Showcase
====================

A clean, modular, and professional A/B testing toolkit in Python.
Demonstrates both frequentist and Bayesian approaches for portfolio projects.
"""

from .data_generator import generate_ab_data
from .frequentist import run_frequentist_test
from .bayesian import run_bayesian_test
from .visualization import plot_conversion_rates, plot_posterior

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "Professional A/B Testing Showcase - Frequentist + Bayesian"

# Public API
__all__ = [
    "generate_ab_data",
    "run_frequentist_test",
    "run_bayesian_test",
    "plot_conversion_rates",
    "plot_posterior",
]
