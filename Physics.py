# Constants
m = 9.109e-31  # Mass of electron/positron (kg)
q = 1.602e-19  # Charge of electron/positron (C)

# User input for parameters
B = float(input("Enter magnetic field strength (in mT): ")) * 1e-3  # Convert to Tesla
KE = float(input("Enter kinetic energy (in eV): ")) * 1.602e-19  # Convert to Joules
total_time = float(input("Enter total simulation time (in µs): ")) * 1e-6  # Convert to seconds

# Derived quantities
v0 = (2 * KE / m) ** 0.5  # Initial velocity (m/s)
dt = 1e-9  # Time step (s)
num_steps = int(total_time / dt)  # Number of steps

# Initial conditions
pos_x = [0]  # Initial x position
pos_y = [0]  # Initial y position
vel_x = [v0]  # Initial x velocity
vel_y = [0]  # Initial y velocity

# Simulate motion using the Lorentz force
for _ in range(num_steps):
    # Lorentz force: F = q(v × B)
    Fx = -q * vel_y[-1] * B  # Force in x-direction
    Fy = q * vel_x[-1] * B  # Force in y-direction

    # Update velocity using Euler's method
    vx_new = vel_x[-1] + (Fx / m) * dt
    vy_new = vel_y[-1] + (Fy / m) * dt

    # Update position
    x_new = pos_x[-1] + vel_x[-1] * dt
    y_new = pos_y[-1] + vel_y[-1] * dt

    # Append new position and velocity
    pos_x.append(x_new)
    pos_y.append(y_new)
    vel_x.append(vx_new)
    vel_y.append(vy_new)

# Plot the trajectory using ASCII art
print("\nTrajectory of the particle (simplified ASCII plot):")
x_min, x_max = min(pos_x), max(pos_x)
y_min, y_max = min(pos_y), max(pos_y)

# Scaling with zero-division protection
scale_x = 50 / (x_max - x_min + 1e-9)  # Avoid division by zero
scale_y = 20 / (y_max - y_min + 1e-9)  # Avoid division by zero

# Create empty grid
grid = [[" " for _ in range(51)] for _ in range(21)]

# Map trajectory to grid
for x, y in zip(pos_x, pos_y):
    grid_x = max(0, min(50, int((x - x_min) * scale_x)))  # Clamp within bounds
    grid_y = max(0, min(20, int((y - y_min) * scale_y)))  # Clamp within bounds
    grid[20 - grid_y][grid_x] = "*"  # Flip y-axis for correct display

# Print ASCII plot
for row in grid:
    print("".join(row))

# Export trajectory data to a CSV file
with open("trajectory_data.csv", "w") as file:
    file.write("x,y\n")
    for x, y in zip(pos_x, pos_y):
        file.write(f"{x},{y}\n")

print("\nTrajectory data saved to 'trajectory_data.csv'.")
