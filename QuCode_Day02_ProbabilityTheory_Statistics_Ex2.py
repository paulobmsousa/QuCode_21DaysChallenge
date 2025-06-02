# Basic Probability: Rolling a fair six-sided die
prob_rolling_4 = 1 / 6
print("Probability of rolling a 4:", prob_rolling_4)

# Manual calculation for mean and standard deviation of a small dataset
data = [40, 45, 50, 55, 60]  # Example dataset
size = len(data)

# Calculate mean
sum_values = 0
for value in data:
    sum_values += value
mean = sum_values / size

# Calculate standard deviation (manual implementation)
sum_squared_differences = 0
for value in data:
    sum_squared_differences += (value - mean) ** 2

std_dev = (sum_squared_differences / size) ** 0.5

print("Sample mean:", mean)
print("Sample standard deviation:", std_dev)

# Bayes' Theorem Example (manually calculated)
P_Disease = 1 / 100  # 1% probability
P_Positive_given_Disease = 99 / 100  # 99% accuracy
P_Positive_given_No_Disease = 5 / 100  # 5% false positives

# Calculate total probability of testing positive
P_Positive = (P_Positive_given_Disease * P_Disease) + (P_Positive_given_No_Disease * (1 - P_Disease))

# Bayes' Theorem Calculation
P_Disease_given_Positive = (P_Positive_given_Disease * P_Disease) / P_Positive

print("Probability of having the disease given a positive test:", P_Disease_given_Positive)
