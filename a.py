import matplotlib.pyplot as plt
import numpy as np

# Simulate temperature data for 30 days (in degrees Celsius)
np.random.seed(42)  # For reproducibility
days = np.arange(1, 31)  # Days from 1 to 30
temperatures = np.random.uniform(
    low=15, high=35, size=len(days)
)  # Random temps between 15°C and 35°C

# Print the first few values to verify
print("Days:", days[:5])
print("Temperatures:", temperatures[:5])


# Create the plot
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(days, temperatures, marker="o", linestyle="-", color="b", label="Temperature")

# Add title and labels
plt.title("Daily Temperature Over One Month", fontsize=16)
plt.xlabel("Day of the Month", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# Add grid and legend
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
