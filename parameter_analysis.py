import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Parameter Analysis of the Fisher-KPP Model
# -------------------------------------------------

# Fixed reaction rate
r = 1.0

# Diffusion coefficients to investigate
D_values = [0.5, 1.0, 2.0]

# Spatial domain
L = 100.0
dx = 0.2
x = np.arange(0, L + dx, dx)

# Time parameters
dt = 0.01
T = 20.0
num_steps = int(T / dt)

# Store calculated propagation speeds
results = []

for D in D_values:

    # Sigmoid traveling-front initial condition
    u = 1.0 / (1.0 + np.exp((x - 20.0) / 2.0))

    wave_positions = []

    for n in range(1, num_steps + 1):

        u_xx = np.zeros_like(u)

        # Second spatial derivative
        u_xx[1:-1] = (
            u[2:] - 2 * u[1:-1] + u[:-2]
        ) / dx**2

        # Fisher-KPP equation
        u_new = u + dt * (
            D * u_xx + r * u * (1 - u)
        )

        # Boundary conditions
        u_new[0] = 1.0
        u_new[-1] = 0.0

        u = u_new

        # Record front position every 2 time units
        if n % int(2.0 / dt) == 0:

            front_index = np.argmin(
                np.abs(u - 0.5)
            )

            wave_positions.append(
                x[front_index]
            )

    # Include initial front position
    initial_front = np.argmin(
        np.abs(
            (1.0 / (1.0 + np.exp((x - 20.0) / 2.0))) - 0.5
        )
    )

    positions = np.array(
        [x[initial_front]] + wave_positions
    )

    times = np.arange(
        0, T + 2, 2
    )

    # Calculate propagation speed
    speed, intercept = np.polyfit(
        times, positions, 1
    )

    results.append((D, speed))

    print(
        f"D = {D:.1f} | "
        f"Estimated propagation speed = "
        f"{speed:.4f}"
    )

# -------------------------------------------------
# Plot parameter comparison
# -------------------------------------------------

D_array = np.array([item[0] for item in results])
speed_array = np.array([item[1] for item in results])

plt.figure(figsize=(8, 6))

plt.plot(
    D_array,
    speed_array,
    marker="o"
)

plt.xlabel("Diffusion coefficient D")
plt.ylabel("Propagation speed")
plt.title(
    "Effect of Diffusion Coefficient on Wave Propagation"
)

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "diffusion_parameter_analysis.png",
    dpi=300
)

plt.show()
