# Mathematical Modeling of Wave Propagation in Biological Systems
A mathematical modeling study of wave propagation in biological systems using nonlinear partial differential equations
## 1. Introduction

Wave propagation is an important phenomenon in many biological systems, including excitable tissues and neural systems. Mathematical models based on partial differential equations provide a useful framework for studying how biological signals propagate through space and evolve over time.

This project investigates wave propagation using a nonlinear reaction-diffusion partial differential equation. The aim is to develop a mathematical model, perform numerical simulations, and analyze how changes in model parameters influence wave behavior.

## 2. Research Question

How can nonlinear partial differential equations be used to mathematically model and analyze wave propagation in biological systems?

## 3. Objectives

The main objectives of this project are:

1. To formulate a nonlinear mathematical model for biological wave propagation.
2. To solve the model numerically.
3. To visualize the propagation of biological waves.
4. To investigate the influence of model parameters on wave behavior.
5. To discuss the potential relevance of reaction-diffusion models to biological systems.

## 4. Mathematical Model

To investigate biological wave propagation, this project considers the Fisher-KPP reaction-diffusion equation:

$$
\frac{\partial u}{\partial t} = D\frac{\partial^2 u}{\partial x^2}+ ru(1-u)$$

where:

- $u(x,t)$ represents the normalized biological activity or signal.
- $D$ is the diffusion coefficient.
- $r$ is the reaction or growth parameter.
- $x$ represents the spatial coordinate.
- $t$ represents time.

The diffusion term describes the spatial spreading of the biological signal, while the nonlinear reaction term represents local changes in biological activity.

### Model Assumptions

The model assumes that:

1. The biological activity varies continuously in space and time.
2. Spatial propagation can be represented by a diffusion process.
3. Local biological dynamics are represented by a nonlinear reaction term.
4. The model parameters are constant during the simulation.

## 6. Results

The numerical simulation demonstrates the propagation of a localized biological activity profile over time. The solution profiles at different time points show a clear spatial shift of the wave, indicating traveling-wave behavior.

The simulated wave exhibits a broad, plateau-like profile that evolves and propagates through the spatial domain as time increases.

### Wave Propagation

![Numerical simulation of biological wave propagation](initial_gaussian_simulation.png)

**Figure 1.** Numerical simulation showing the propagation of the biological wave profile at different time points.
### Quantitative Analysis of Wave Propagation

The position of the traveling wave front was estimated by tracking the spatial location where the solution satisfies $u = 0.5$.

The simulated front positions were:

| Time | Front Position |
|------|----------------|
| 0 | 20.00 |
| 2 | 24.40 |
| 4 | 29.20 |
| 6 | 34.00 |
| 8 | 39.00 |
| 10 | 44.00 |
| 12 | 49.00 |
| 14 | 54.00 |
| 16 | 58.80 |
| 18 | 63.80 |
| 20 | 68.80 |

A linear fit of front position against time gives an estimated propagation speed of:

$$
c \approx 2.4564
$$

spatial units per time unit.

The increasing front position demonstrates that the modeled biological activity propagates through the spatial domain over time.
