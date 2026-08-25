# Mathematical Analysis of EEG Brain-Wave Activity

## Project Overview

This project investigates frequency characteristics of real electroencephalography (EEG) signals using mathematical and computational methods.

The analysis combines a mathematical background with Python-based signal processing to study the distribution of EEG frequency components, with particular attention to the theta band (4–8 Hz).

Real EEG data from the PhysioNet EEG Motor Movement/Imagery Dataset were used for the analysis.

---

## Research Objective

The main objective of this project is to analyze the spectral characteristics of EEG signals and quantify the contribution of different frequency bands.

The project focuses on:

- EEG signal preprocessing
- Frequency-domain analysis
- Power spectral density
- Delta, theta, alpha, and beta band power
- Relative frequency-band power
- Time-frequency analysis
- Multi-channel theta comparison
- Statistical and mathematical analysis of EEG features

---

## Dataset

The EEG recordings were obtained from the PhysioNet EEG Motor Movement/Imagery Dataset.

Each recording contains:

- 64 EEG channels
- Sampling frequency of 160 Hz
- EEG recordings in EDF+ format
- Event annotations

Dataset:

https://physionet.org/content/eegmmidb/1.0.0/

---

## Tools and Technologies

The project was developed using:

- Python
- NumPy
- Matplotlib
- MNE-Python
- Fast Fourier Transform (FFT)
- Welch Power Spectral Density estimation
- Statistical analysis

---

## Methodology

### 1. EEG Data Loading

The EEG recording was loaded using MNE-Python.

The C3 EEG channel was selected for detailed analysis.

### 2. Signal Filtering

A 1–40 Hz band-pass filter was applied to reduce very-low-frequency drift and high-frequency noise.

### 3. Frequency-Domain Analysis

Fast Fourier Transform (FFT) was used to investigate the frequency components of the EEG signal.

### 4. EEG Band-Power Analysis

Power was calculated for four conventional frequency bands:

| Band | Frequency Range |
|---|---|
| Delta | 1–4 Hz |
| Theta | 4–8 Hz |
| Alpha | 8–13 Hz |
| Beta | 13–30 Hz |

### 5. Relative Band Power

Relative power was calculated as:

Relative Power = Band Power / Total Power × 100

This allowed comparison of the contribution of each frequency band.

### 6. Time-Frequency Analysis

A spectrogram was generated to examine how the frequency content of the EEG signal changes over time.

### 7. Multi-Channel Analysis

Theta-band relative power was compared across five EEG channels:

- C3
- C4
- Fz
- Pz
- Oz

### 8. Mathematical Analysis

Mean, standard deviation, range, and coefficient of variation were calculated to quantify the spatial variation of theta-band activity.

---

## Results

### C3 Frequency-Band Analysis

The relative power obtained from the C3 channel was:

| Frequency Band | Relative Power |
|---|---:|
| Delta | 52.25% |
| Theta | 20.59% |
| Alpha | 13.66% |
| Beta | 13.50% |

The theta band accounted for **20.59%** of the combined power of the analyzed frequency bands in the C3 channel.

### Multi-Channel Theta Analysis

| EEG Channel | Theta Relative Power |
|---|---:|
| C3 | 20.59% |
| C4 | 18.66% |
| Fz | 20.12% |
| Pz | 16.74% |
| Oz | 14.82% |

Theta relative power ranged from **14.82% to 20.59%** across the five analyzed channels.

### Mathematical Results

| Measure | Value |
|---|---:|
| Mean theta power | 18.19% |
| Standard deviation | 2.41% |
| Minimum | 14.82% |
| Maximum | 20.59% |
| Range | 5.77% |
| Coefficient of variation | 13.23% |

C3 showed the highest observed theta relative power, while Oz showed the lowest among the five selected channels.

---

## Figures

### Relative EEG Band Power

`C3_relative_band_power.png`

### Time-Frequency Analysis

`C3_EEG_spectrogram.png`

### Multi-Channel Theta Comparison

`final_theta_comparison.png`

---

## Interpretation

The analysis demonstrates that EEG signals contain measurable contributions from multiple frequency bands.

The theta-band contribution varied across the selected EEG channels, with the highest observed value at C3 and the lowest at Oz.

The calculated mean and standard deviation provide a simple mathematical description of the variation in theta-band relative power across the selected electrode locations.

These findings demonstrate how mathematical and computational methods can be applied to extract quantitative features from biological signals.

---

## Limitations

This project is an exploratory analysis based on a single EEG recording and five selected channels.

Therefore, the results should not be interpreted as clinical findings or generalized to a wider population.

Further analysis using multiple subjects, multiple recordings, and task-specific event segments would be required for broader conclusions.

---

## Future Work

Possible extensions include:

- Analysis of multiple subjects
- Automated EEG artifact removal
- Comparison of resting and motor-imagery periods
- Analysis of additional EEG channels
- Statistical comparison between experimental conditions
- Machine-learning-based EEG classification
- Mathematical modeling of brain-wave propagation
- Comparison of experimental EEG characteristics with mathematical models

---

## Project Significance

This project demonstrates the application of mathematical analysis, numerical methods, and Python-based computational tools to real biological data.

It provides an interdisciplinary connection between:

**Mathematics + Computer Science + Neuroscience + Biological Signal Processing**

---

## Author

Darain Fatima

MPhil Mathematics — Applied Mathematics

Research interests include nonlinear partial differential equations, mathematical modeling, symmetry analysis, and computational approaches to biological systems.