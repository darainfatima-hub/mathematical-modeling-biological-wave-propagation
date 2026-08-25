import numpy as np

# -----------------------------------------
# Theta relative power from EEG channels
# -----------------------------------------

channels = np.array([
    "C3",
    "C4",
    "Fz",
    "Pz",
    "Oz"
])

theta_power = np.array([
    20.59,
    18.66,
    20.12,
    16.74,
    14.82
])

# -----------------------------------------
# Mathematical statistics
# -----------------------------------------

mean_theta = np.mean(theta_power)

std_theta = np.std(
    theta_power,
    ddof=1
)

minimum = np.min(theta_power)

maximum = np.max(theta_power)

range_theta = maximum - minimum

coefficient_variation = (
    std_theta / mean_theta
) * 100

# -----------------------------------------
# Display results
# -----------------------------------------

print("\nMATHEMATICAL ANALYSIS")
print("=" * 40)

print(
    f"Mean theta power = "
    f"{mean_theta:.2f}%"
)

print(
    f"Standard deviation = "
    f"{std_theta:.2f}%"
)

print(
    f"Minimum theta power = "
    f"{minimum:.2f}%"
)

print(
    f"Maximum theta power = "
    f"{maximum:.2f}%"
)

print(
    f"Theta range = "
    f"{range_theta:.2f}%"
)

print(
    f"Coefficient of variation = "
    f"{coefficient_variation:.2f}%"
)

# -----------------------------------------
# Channel with maximum theta power
# -----------------------------------------

max_index = np.argmax(theta_power)

print(
    f"\nHighest theta power: "
    f"{channels[max_index]} "
    f"({theta_power[max_index]:.2f}%)"
)

# -----------------------------------------
# Channel with minimum theta power
# -----------------------------------------

min_index = np.argmin(theta_power)

print(
    f"Lowest theta power: "
    f"{channels[min_index]} "
    f"({theta_power[min_index]:.2f}%)"
)