import mne
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Load real EEG data
# -------------------------------------------------

file_path = "data/S001R01.edf"

raw = mne.io.read_raw_edf(
    file_path,
    preload=True
)

sfreq = raw.info["sfreq"]

# -------------------------------------------------
# Channels to analyze
# -------------------------------------------------

channels = [
    "C3..",
    "C4..",
    "Fz..",
    "Pz..",
    "Oz.."
]

# -------------------------------------------------
# EEG frequency bands
# -------------------------------------------------

bands = {
    "Delta": (1, 4),
    "Theta": (4, 8),
    "Alpha": (8, 13),
    "Beta": (13, 30)
}

theta_relative_power = {}

# -------------------------------------------------
# Analyze each channel
# -------------------------------------------------

for channel in channels:

    print(f"\nAnalyzing {channel}...")

    data = raw.get_data(
        picks=[channel]
    )[0]

    # Filter signal
    filtered_data = mne.filter.filter_data(
        data,
        sfreq=sfreq,
        l_freq=1.0,
        h_freq=40.0,
        verbose=False
    )

    # Calculate PSD
    psd, frequencies = mne.time_frequency.psd_array_welch(
        filtered_data,
        sfreq=sfreq,
        fmin=1,
        fmax=40,
        n_fft=2048,
        verbose=False
    )

    band_power = {}

    # Calculate power for each band
    for band, (low, high) in bands.items():

        mask = (
            (frequencies >= low) &
            (frequencies < high)
        )

        power = np.trapezoid(
            psd[mask],
            frequencies[mask]
        )

        band_power[band] = power

    # Total power
    total_power = sum(
        band_power.values()
    )

    # Theta relative power
    theta_percentage = (
        band_power["Theta"] /
        total_power
    ) * 100

    theta_relative_power[channel] = theta_percentage

    print(
        f"Theta relative power = "
        f"{theta_percentage:.2f}%"
    )

# -------------------------------------------------
# Display final results
# -------------------------------------------------

print("\n" + "=" * 45)
print("THETA RELATIVE POWER BY EEG CHANNEL")
print("=" * 45)

for channel, value in theta_relative_power.items():

    print(
        f"{channel}: {value:.2f}%"
    )

# -------------------------------------------------
# Plot comparison
# -------------------------------------------------

labels = [
    "C3",
    "C4",
    "Fz",
    "Pz",
    "Oz"
]

values = list(
    theta_relative_power.values()
)

plt.figure(figsize=(9, 6))

plt.bar(
    labels,
    values
)

plt.xlabel("EEG Channel")
plt.ylabel("Theta Relative Power (%)")

plt.title(
    "Theta-Band Relative Power Across EEG Channels"
)

plt.grid(
    axis="y"
)

plt.tight_layout()

plt.savefig(
    "theta_channel_comparison.png",
    dpi=300
)

plt.show()