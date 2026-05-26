LePIC+
======

LePIC+ is a modular electrostatic Particle-In-Cell (PIC) plasma simulation
code written in modern Fortran.

The code is designed for plasma source simulations, RF discharges,
ion extraction, and plasma-wall interaction studies.

Features
--------

LePIC currently supports:

* Electrostatic PIC solver
* Modular OOP architecture
* MPI/OpenMP parallelization
* Plasma chemistry and collisions
* RF electron heating
* Multiple boundary conditions
* 2D diagnostic plane outputs
* Modern CMake build system

The code is being developed for ion source simulations and numerical plasma physics research.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   overview
   installation
   quickstart
   running
   inputs
   outputs

.. toctree::
   :maxdepth: 2
   :caption: Physics and Numerics

   physics
   modules
   code_structure

.. toctree::
   :maxdepth: 2
   :caption: Development

   developers
   readthedocs
