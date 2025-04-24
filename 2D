import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Constants and Parameters ---
# Particle (Electron)
q = -1.60217663e-19  # Charge (C)
m = 9.1093837e-31   # Mass (kg)
KE_eV = 20.0          # Kinetic Energy (eV)

# Geometry
L_cyl = 0.3556       # Cylinder length (m)
R_cyl = 0.0762       # Cylinder radius (m)
slit_H = 0.0889      # Slit height (m)
slit_W = 0.0508      # Slit width (m) - not used in y-z plot
beam_radius = 0.002 # Beam radius (m)

# Slit position (midway along length, attached to top)
z_slit = L_cyl / 2.0
y_slit_top = R_cyl
y_slit_bottom = y_slit_top - slit_H # = 0.0762 - 0.0889 = -0.0127 m

# Chosen Field Parameters (adjust as needed)
Bx = -0.00127  # Magnetic field in x (T)
Ey = 9020.0    # Electric field in y (V/m)

# --- Calculations ---
KE_J = KE_eV * abs(q) # Convert eV to Joules
v0 = np.sqrt(2 * KE_J / m) # Initial velocity (m/s)

# Check if fields are non-zero
if Bx == 0:
    print("Error: Bx cannot be zero for this solution.")
    exit()

omega_c = q * Bx / m # Cyclotron frequency (rad/s)

# Time and length of field interaction (using n=1 cycle)
T_field = 2 * np.pi / abs(omega_c)
L_field_calc = abs(- (2 * np.pi * m * Ey) / (q * Bx**2)) # Calculated field length
# Use a fixed desired field length for positioning
L_field = 0.20 # Desired Field length (m) - Should ideally match L_field_calc

# Define field region boundaries
z_start = z_slit - L_field / 2.0
z_end = z_slit + L_field / 2.0

# Check parameters
y_peak_calc = (2*m / (q * Bx)) * (v0 + Ey / Bx)
print(f"--- Simulation Parameters ---")
print(f"Particle: Electron")
print(f"Initial Velocity (v0): {v0:.3e} m/s")
print(f"Fields: Bx = {Bx:.4f} T, Ey = {Ey:.1f} V/m")
print(f"Field Region: z = {z_start:.4f} m to {z_end:.4f} m (Length = {L_field:.4f} m)")
print(f"Calculated Omega_c: {omega_c:.3e} rad/s")
print(f"Calculated Time in Field (T): {T_field:.3e} s")
print(f"Calculated Required L_field for T: {L_field_calc:.4f} m")
print(f"Calculated Peak Deflection (y_peak): {y_peak_calc:.4f} m")
print(f"Slit bottom edge: y = {y_slit_bottom:.4f} m")
print(f"Required clearance (slit + beam radius): y < {y_slit_bottom - beam_radius:.4f} m")

if abs(y_peak_calc) < abs(y_slit_bottom - beam_radius):
    print("WARNING: Calculated peak deflection may not be enough to clear slit!")
if abs(y_peak_calc) + beam_radius > R_cyl:
    print("WARNING: Calculated peak deflection may hit cylinder wall!")
if not np.isclose(L_field, L_field_calc, rtol=0.01):
     print(f"WARNING: Chosen L_field {L_field:.4f} differs from L_field_calc {L_field_calc:.4f} for perfect return.")


# --- Trajectory Simulation ---
# Time points for simulation within the field
num_points_field = 200
t_prime = np.linspace(0, T_field, num_points_field) # Time relative to entering field

# Calculate trajectory within the field region
y_field = (m / (q * Bx)) * (v0 + Ey / Bx) * (1 - np.cos(omega_c * t_prime))
z_relative = (m / (q * Bx)) * (v0 + Ey / Bx) * np.sin(omega_c * t_prime) - (Ey / Bx) * t_prime
z_field = z_start + z_relative

# Ensure z_field ends correctly (due to potential mismatch L_field vs L_field_calc)
# Use the calculated endpoint based on time T_field
z_end_calc = z_start + z_relative[-1]


# Combine trajectory parts
# Part 1: Before field (z=0 to z=z_start)
z_before = np.linspace(0, z_start, 50)
y_before = np.zeros_like(z_before)

# Part 2: Inside field (using calculated points)
# Make sure z_field is monotonically increasing - necessary if using analytical path
# (It should be for these parameters, but good practice to check for complex cases)
sort_indices = np.argsort(z_field)
z_field_sorted = z_field[sort_indices]
y_field_sorted = y_field[sort_indices]
# Filter out any points outside the intended z range if L_field mismatch is large
valid_idx = (z_field_sorted >= z_start) & (z_field_sorted <= z_end) # Use intended end point
z_field_final = z_field_sorted[valid_idx]
y_field_final = y_field_sorted[valid_idx]


# Part 3: After field (z=z_end to z=L_cyl)
# Start from the *actual* exit position/angle from the field segment
y_exit = y_field_final[-1] if len(y_field_final)>0 else 0 # Should be near 0
z_after = np.linspace(z_end, L_cyl, 50)
y_after = np.full_like(z_after, y_exit) # Assume it continues straight from exit y


# Full trajectory
z_traj = np.concatenate((z_before, z_field_final, z_after))
y_traj = np.concatenate((y_before, y_field_final, y_after))


# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 5))

# Plot trajectory
ax.plot(z_traj, y_traj, label='Electron Beam Center', color='blue')

# Plot beam width representation (optional, illustrative)
ax.fill_between(z_traj, y_traj - beam_radius, y_traj + beam_radius, color='blue', alpha=0.2, label='Beam Extent')


# Plot cylinder boundaries
ax.axhline(R_cyl, color='gray', linestyle='--', label='Cylinder Wall')
ax.axhline(-R_cyl, color='gray', linestyle='--')

# Plot slit obstacle
slit_rect = patches.Rectangle((z_slit - slit_W/2, y_slit_bottom), slit_W, slit_H,
                               linewidth=1, edgecolor='red', facecolor='red', alpha=0.5, label='Slit Obstacle')
ax.add_patch(slit_rect)

# Plot Field Region boundaries
ax.axvline(z_start, color='green', linestyle=':', label='E/B Field Region Start')
ax.axvline(z_end, color='green', linestyle=':', label='E/B Field Region End')


# Formatting
ax.set_xlabel("Position z (m)")
ax.set_ylabel("Position y (m)")
ax.set_title(f"Electron Beam Trajectory ($E_y={Ey:.0f}$ V/m, $B_x={Bx*1000:.2f}$ mT)")
ax.set_xlim(0, L_cyl)
ax.set_ylim(-R_cyl * 1.1, R_cyl * 1.1)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize='small')
ax.set_aspect('equal', adjustable='box') # Make aspect ratio equal for visual accuracy
plt.tight_layout()
plt.show()
