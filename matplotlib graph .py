import numpy as np
import matplotlib.pyplot as plt

# Define the equation x^2 + y + 3 = 0
# Rearrange to y = -x^2 - 3
def equation(x):
    return -x**2 - 3

# Generate x values
x = np.linspace(-20, 20)  # Range of x values it can be any  but +ve and -ve value will be same

# Calculate y values
y = equation(x)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$x^2 + y + 3 = 0$")
plt.axhline(0, color='black', linewidth=0.2, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # y-axis
plt.title("Graph of $x^2 + y + 3 = 0$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()