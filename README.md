# Mathematical Modeling and Analysis of Biological Waves

## Overview

This repository contains two interconnected computational projects developed around mathematical modeling, numerical simulation, and analysis of biological wave phenomena.

The first part focuses on mathematical modeling of biological wave propagation using the Fisher-KPP reaction-diffusion equation.

The second part extends the computational work toward real biological signals by analyzing EEG brain-wave activity using mathematical and signal-processing techniques.

Together, the projects demonstrate an interdisciplinary connection between:

**Applied Mathematics + Numerical Methods + Python + Biological Modeling + EEG Signal Processing + Neuroscience**

---

# Project 1 — Mathematical Modeling of Biological Wave Propagation

## Overview

This project investigates the propagation of biological waves using mathematical modeling and numerical simulation.

The Fisher-KPP reaction-diffusion equation is used as a mathematical framework for studying the evolution and propagation of a biological activity profile.

The model is based on the reaction-diffusion equation:

$$
u_t = D u_{xx} + r u(1-u)
$$

where:

- $u(x,t)$ represents biological activity
- $D$ is the diffusion coefficient
- $r$ is the reaction rate
- $x$ represents spatial position
- $t$ represents time

---

## Numerical Simulation

The Fisher-KPP equation was solved numerically using an explicit finite-difference scheme.

The simulation investigates how an initially localized biological activity profile propagates through space over time.

### Main Python script

`simulation.py`

### Travelling-wave simulation

![Travelling Wave](travelling_wave.png)

---

## Diffusion Parameter Analysis

Different diffusion coefficients were investigated to examine their influence on propagation speed.

The investigated values were:

- $D = 0.5$
- $D = 1.0$
- $D = 2.0$

### Parameter analysis

`parameter_analysis.py`

![Diffusion Parameter Analysis](diffusion_parameter_analysis.png)

---

## Initial Gaussian Simulation

An additional numerical simulation was performed using a localized initial profile.

![Initial Gaussian Simulation](initial_gaussian_simulation.png)

---

## Mathematical Results

The position of the traveling front was estimated using the point where:

$$
u(x,t) \approx 0.5
$$

The propagation speed was then estimated using linear regression of front position against time.

The analysis demonstrates how numerical methods can be used to investigate wave propagation in reaction-diffusion systems.

---

# Project 2 — Mathematical Analysis of EEG Brain-Wave Activity

## Overview

The second project applies mathematical and computational methods to real EEG data.

The objective is to analyze the frequency characteristics of EEG signals and quantify the contribution of different frequency bands, with particular attention to the theta band.

Real EEG data were obtained from the PhysioNet EEG Motor Movement/Imagery Dataset.

Dataset:

https://physionet.org/content/eegmmidb/1.0.0/

---

## Dataset

The EEG recording used in this analysis contains:

- 64 EEG channels
- Sampling frequency of 160 Hz
- EDF+ format
- Event annotations

The analysis was initially performed using the `S001R01.edf` recording.

---

## EEG Analysis Pipeline

The analysis consists of:

1. Loading the EEG signal
2. Selecting EEG channels
3. Signal filtering
4. Frequency-domain analysis
5. Power spectral density analysis
6. EEG frequency-band analysis
7. Relative band-power calculation
8. Time-frequency analysis
9. Multi-channel theta analysis
10. Mathematical statistical analysis

---

## EEG Frequency Bands

Four conventional EEG frequency bands were investigated:

| Band | Frequency Range |
|---|---|
| Delta | 1–4 Hz |
| Theta | 4–8 Hz |
| Alpha | 8–13 Hz |
| Beta | 13–30 Hz |

---

## C3 EEG Band-Power Analysis

The C3 channel was selected for detailed frequency-band analysis.

### Relative Power

| Frequency Band | Relative Power |
|---|---:|
| Delta | 52.25% |
| Theta | 20.59% |
| Alpha | 13.66% |
| Beta | 13.50% |

![C3 Relative Band Power](C3_relative_band_power.png)

---

## Time-Frequency Analysis

A spectrogram was generated to investigate changes in EEG frequency content over time.

![C3 EEG Spectrogram](C3_EEG_spectrogram.png)

---

## Multi-Channel Theta Analysis

Theta relative power was compared across five selected EEG channels.

| Channel | Theta Relative Power |
|---|---:|
| C3 | 20.59% |
| C4 | 18.66% |
| Fz | 20.12% |
| Pz | 16.74% |
| Oz | 14.82% |

![Theta Comparison](final_theta_comparison.png)

---

## Mathematical Analysis of Theta Activity

The following statistical measures were calculated:

| Measure | Result |
|---|---:|
| Mean theta power | 18.19% |
| Standard deviation | 2.41% |
| Minimum | 14.82% |
| Maximum | 20.59% |
| Range | 5.77% |
| Coefficient of variation | 13.23% |

The highest observed theta relative power was found at C3 (20.59%), while the lowest was observed at Oz (14.82%).

---

# Python Implementation

The main Python scripts are:

### Biological Wave Modeling

- `simulation.py`
- `parameter_analysis.py`

### EEG Analysis

- `eeg_analysis.py`
- `final_results.py`
- `mathematical_analysis.py`

---

# Technologies Used

- Python
- NumPy
- Matplotlib
- MNE-Python
- Numerical finite-difference methods
- Fast Fourier Transform (FFT)
- Power spectral density analysis
- Statistical analysis
- Reaction-diffusion modeling

---

# Scientific Significance

These projects demonstrate the use of mathematical and computational techniques for studying biological phenomena.

The work connects mathematical modeling with real biological data through two complementary approaches:

**Mathematical model → Biological wave propagation**

and

**Real EEG data → Mathematical signal analysis**

This provides an interdisciplinary framework connecting:

**Applied Mathematics + Computer Science + Physics + Biology + Neuroscience**

---

# Limitations

The EEG analysis presented here is exploratory and is based on a limited number of selected channels and recordings.

The results should not be interpreted as clinical findings.

Further work using multiple subjects, multiple experimental conditions, and larger datasets would provide a stronger basis for statistical conclusions.

---

# Future Work

Future extensions may include:

- Analysis of multiple EEG subjects
- Event-based EEG segmentation
- Comparison of motor-imagery conditions
- Automated artifact removal
- Machine-learning classification
- Mathematical modeling of EEG wave propagation
- Comparison between theoretical biological-wave models and experimental EEG signals
- Development of more advanced mathematical models for biological systems

---

# Author

**Darain Fatima**

MPhil Mathematics — Applied Mathematics

Research interests include:

- Nonlinear partial differential equations
- Mathematical modeling
- Symmetry analysis
- Reaction-diffusion equations
- Biological wave propagation
- EEG signal analysis
- Computational mathematics