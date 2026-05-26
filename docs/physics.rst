Physics Model
=============

LePIC uses the electrostatic Particle-In-Cell (PIC) method.

Main Components
---------------

* Particle pusher
* Charge deposition
* Poisson solver
* Boundary conditions
* Plasma chemistry
* Coulomb collisions
* RF electron heating

Particle Mover
--------------

Particles are advanced using the Lorentz force equation.

Poisson Solver
--------------

The electrostatic potential is computed from Poisson's equation:

.. math::

   \nabla^2 \phi = -\rho / \epsilon_0
