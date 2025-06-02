import numpy as np
import scipy.stats as stats

# Basic Probability: Probability of an event occurring
# Example: Rolling a fair six-sided die and getting a "4"
prob_rolling_4 = 1 / 6
print(f"Probability of rolling a 4: {prob_rolling_4}")

# Probability Distributions: Normal distribution example
# Generating a normal distribution with mean 50 and standard deviation 10
mean, std_dev = 50, 10
data = np.random.normal(mean, std_dev, 1000)  # Simulating 1000 values
print(f"Sample mean: {np.mean(data):.2f}, Sample std dev: {np.std(data):.2f}")

# Plotting the probability density function (requires matplotlib)
import matplotlib.pyplot as plt
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
pdf = stats.norm.pdf(x, mean, std_dev)

plt.plot(x, pdf, label="Normal Distribution")
plt.hist(data, bins=30, density=True, alpha=0.5, label="Sample Data Histogram")
plt.legend()
plt.title("Normal Distribution Example")
plt.show()

# Bayes' Theorem Example:
# Suppose a test detects a rare disease with 99% accuracy, but the disease is only present in 1% of the population
P_Disease = 0.01  # Prior probability of disease
P_Positive_given_Disease = 0.99  # Probability of testing positive if disease is present
P_Positive_given_No_Disease = 0.05  # False positive rate

# Applying Bayes' theorem:
# P(Disease | Positive) = P(Positive | Disease) * P(Disease) / P(Positive)
P_Positive = (P_Positive_given_Disease * P_Disease) + (P_Positive_given_No_Disease * (1 - P_Disease))
P_Disease_given_Positive = (P_Positive_given_Disease * P_Disease) / P_Positive

print(f"Probability of having the disease given a positive test result: {P_Disease_given_Positive:.3f}")
