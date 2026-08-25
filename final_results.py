import matplotlib.pyplot as plt

# -----------------------------------------
# Final EEG Results
# -----------------------------------------

channels = ["C3", "C4", "Fz", "Pz", "Oz"]

theta_power = [
    20.59,
    18.66,
    20.12,
    16.74,
    14.82
]

# -----------------------------------------
# Plot
# -----------------------------------------

plt.figure(figsize=(9, 6))

plt.bar(channels, theta_power)

plt.xlabel("EEG Channel")
plt.ylabel("Theta Relative Power (%)")

plt.title(
    "Theta-Band Relative Power Across EEG Channels"
)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig(
    "final_theta_comparison.png",
    dpi=300
)

plt.show()

# -----------------------------------------
# Print final results
# -----------------------------------------

print("\nFINAL THETA-BAND RESULTS")

for channel, value in zip(
    channels,
    theta_power
):
    print(
        f"{channel}: {value:.2f}%"
    )

print(
    "\nTheta range: "
    f"{min(theta_power):.2f}% - "
    f"{max(theta_power):.2f}%"
)