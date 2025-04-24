# Project-physics
# Electron Beam Trajectory Simulation in a Cylindrical Guide with Slit

This repository contains two Python scripts that simulate the trajectory of an electron beam passing through a cylindrical guide with a slit, under the influence of a constant magnetic field in the x-direction ($B_x$) and a constant electric field in the y-direction ($E_y$).

## Overview

The simulation tracks the electron's motion in the y-z plane (2D) and in 3D space, considering the cylindrical geometry and the presence of a slit obstacle. The scripts calculate the electron's trajectory based on its initial kinetic energy and the applied electromagnetic fields.

### `electron_trajectory_2d.py`

This script simulates and visualizes the electron beam trajectory in the y-z plane. It includes:

- **Constants and Parameters:** Defines physical constants (electron charge and mass), simulation geometry (cylinder dimensions, slit dimensions and position, beam radius), and electromagnetic field parameters.
- **Calculations:** Converts kinetic energy from eV to Joules, calculates the initial velocity, cyclotron frequency, and the electron's trajectory within and outside the field region.
- **Plotting:** Generates a 2D plot showing:
    - The electron beam's center trajectory.
    - An optional representation of the beam's extent.
    - The boundaries of the cylindrical guide.
    - The position and dimensions of the slit obstacle.
    - The region where the electric and magnetic fields are applied.
- **Warnings:** Prints warnings if the calculated peak deflection might not clear the slit or might hit the cylinder wall, and if the chosen field length deviates significantly from the calculated length for a perfect return.

### `electron_trajectory_3d.py`

This script extends the simulation to 3D, visualizing the trajectory within the cylindrical volume. It includes:

- **Constants and Parameters:** Similar to the 2D script.
- **Calculations:** Calculates the trajectory in 3D space (x, y, z) under the influence of the fields. Since the initial velocity is assumed to be along the z-axis and the fields are in the x and y directions, the x-component of the motion remains zero.
- **3D Plotting:** Creates a 3D visualization showing:
    - The cylindrical guide as a semi-transparent surface.
    - The electron beam's center trajectory in 3D space.
    - The slit as a planar obstacle.

## Usage

To run the simulations, you need to have Python installed along with the following libraries:

- **NumPy:** For numerical computations.
- **Matplotlib:** For plotting and visualization.
- **mpl_toolkits.mplot3d:** For 3D plotting (required for `electron_trajectory_3d.py`).

You can install these libraries using pip:

```bash
pip install numpy matplotlib
