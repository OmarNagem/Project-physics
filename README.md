# Project-physics
# Particle Beam Bending with E and B Fields

This project simulates how a 20 eV electron or positron beam bends around an obstacle using electric and magnetic fields, and generates a Word document explaining the full physics and math behind the motion.

## Description

- The beam is 6 mm in diameter and travels along a cylindrical path.
- A rectangular slit (5.08 cm wide, 8.89 cm tall) is located midway through the cylinder.
- A 3-inch radius space is used to bend the beam around the slit and back onto its original path.
- We use a combination of electric fields (Ex) and magnetic bending (Bz) to control the beam trajectory.

## Physics Background

The trajectory of the particle is determined by the Lorentz force:

F = q(E + v × B)

kotlin
Copy
Edit

Breaking this down, we analyze the motion component by component:

- In the x-direction:
m * dvx/dt = q((2V)/d + vy * B)

css
Copy
Edit

- In the y-direction:
m * dvy/dt = -q * vx * B

css
Copy
Edit

- In the z-direction:
vz is constant since Ez = 0

markdown
Copy
Edit

We solve these differential equations analytically and generate a professional `.docx` file that contains:

- Full derivations
- All equations from start to finish
- Clean formatting for documentation or presentation
- Final expressions for position and velocity as functions of time

## Output

- `charged_particle_trajectory.docx` – contains all equations, step-by-step derivations, and final results.

## Requirements

- Python 3
- `python-docx` for Word document creation
- `numpy` (optional for numerical calculations)

### Install with:

```bash
pip install python numpy
