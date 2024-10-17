import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data (no headers)
file_path = ""
data = pd.read_csv(file_path, header=None)

# Assign column names X and Y for chart
data.columns = ['X', 'Y']

# Extract independent (X) and dependent (Y) variables
X = data['X']
Y = data['Y']

# Calculate mean of X and Y
X_mean = np.mean(X)
Y_mean = np.mean(Y)

# Calculate covariance of X and Y and variance of X
cov_XY = np.sum((X - X_mean) * (Y - Y_mean)) / len(X)
var_X = np.sum((X - X_mean) ** 2) / len(X)

# Calculate slope (m) and intercept (b)
slope = cov_XY / var_X
intercept = Y_mean - slope * X_mean

# Print the model parameters
print(f"Slope (m): {slope}")
print(f"Intercept (b): {intercept}")

# Plot data points and the regression line
plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X, slope * X + intercept, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.show()
