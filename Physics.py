import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.602e-19  # charge of electron (C)
m = 9.109e-31  # mass of electron (kg)
E_kin = 20 * q  # kinetic energy in joules
v_z = np.sqrt(2 * E_kin / m)  # velocity in z-direction (initial)

# Parameters for fields
B = 0.01  # Tesla
omega_c = q * B / m  # cyclotron frequency
E_x = 1000  # V/m
a = q * E_x / m  # acceleration due to electric field

# Time parameters
t_max = 2 * np.pi / omega_c  # one cyclotron period
t = np.linspace(0, t_max, 1000)

# Motion equations (cycloidal)
x = (a / omega_c**2) * (1 - np.cos(omega_c * t))
y = (a / omega_c**2) * (np.sin(omega_c * t) - omega_c * t)
z = v_z * t  # linear motion in z

# Plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(z, x, y, label='Beam Trajectory', color='blue')
ax.set_xlabel('z (m)')
ax.set_ylabel('x (m)')
ax.set_zlabel('y (m)')
ax.set_title('Charged Particle Trajectory (E × B Bending)')
ax.legend()
plt.tight_layout()

plt.show()
