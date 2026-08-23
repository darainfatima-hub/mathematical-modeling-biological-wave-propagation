import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Mathematical Modeling of Biological Wave Propagation
# Fisher-KPP Reaction-Diffusion Equation
# -------------------------------------------------

# Model parameters
D = 1.0          # Diffusion coefficient
r = 1.0          # Reaction rate

# Spatial domain
L = 100.0
dx = 0.2
x = np.arange(0, L + dx, dx)

# Time parameters
dt = 0.01
T = 20.0
num_steps = int(T / dt)

# Initial condition: localized biological activity
u = np.exp(-((x - 20.0) ** 2) / 4.0)

# Store selected time snapshots
snapshots = []
snapshot_times = []

# Save initial condition
snapshots.append(u.copy())
snapshot_times.append(0.0)

# Numerical simulation using an explicit finite-difference scheme
for n in range(1, num_steps + 1):

    u_xx = np.zeros_like(u)

    # Second spatial derivative
    u_xx[1:-1] = (u[2:] - 2*u[1:-1] + u[:-2]) / dx**2

    # Reaction-diffusion equation
    u_new = u + dt * (D * u_xx + r * u * (1 - u))

    # Boundary conditions
    u_new[0] = 0.0
    u_new[-1] = 0.0

    u = u_new

    # Store results every 2 time units
    if n % int(2.0 / dt) == 0:
        snapshots.append(u.copy())
        snapshot_times.append(n * dt)

# -------------------------------------------------
# Plot wave propagation
# -------------------------------------------------

plt.figure(figsize=(10, 6))

for profile, time in zip(snapshots, snapshot_times):
    plt.plot(x, profile, label=f"t = {time:.0f}")

plt.xlabel("Spatial position x")
plt.ylabel("Biological activity u(x,t)")
plt.title("Numerical Simulation of Biological Wave Propagation")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("wave_propagation.png", dpi=300)
plt.show()
# -------------------------------------------------
# Estimate wave position and propagation speed
# -------------------------------------------------

wave_positions = []

for profile in snapshots:
    # Position of maximum biological activity
    max_index = np.argmax(profile)
    wave_positions.append(x[max_index])

wave_positions = np.array(wave_positions)

# Calculate propagation speed using linear regression
time_array = np.array(snapshot_times)

speed, intercept = np.polyfit(time_array, wave_positions, 1)

print("\nWave positions:")
for time, position in zip(time_array, wave_positions):
    print(f"t = {time:.1f}, position = {position:.2f}")

print(f"\nEstimated propagation speed = {speed:.4f} spatial units per time unit")
