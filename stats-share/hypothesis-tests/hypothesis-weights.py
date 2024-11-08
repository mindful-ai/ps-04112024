import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv('weights.csv')

# Separate weights by gender
male_weights = data[data['Gender'] == 'Male']['Weight']
female_weights = data[data['Gender'] == 'Female']['Weight']

# Perform two-sample t-test
t_stat, p_value = ttest_ind(male_weights, female_weights, equal_var=False)

# Output results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpret the result
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the average weights.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the average weights.")
