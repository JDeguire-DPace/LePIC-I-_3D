Code structure
==============

The source code is under ``modules/`` and is split into functional areas.

.. code-block:: text

   modules/config/       input and configuration handling
   modules/core/         constants, utilities, RNG, shared state
   modules/fields/       charge deposition, Poisson solver, E and B fields
   modules/geometry/     domain and boundary generation
   modules/io/           2D output routines
   modules/legacy/       legacy numerical routines
   modules/main/         main programs
   modules/particles/    loading, motion, sorting, collisions, reactions, heating
   modules/simulation/   simulation parameters and simulation driver
   modules/test/         test drivers

Main execution path
-------------------

The current main program is ``modules/main/main.f90``. It initializes MPI, creates a ``Simulation`` object, runs the simulation, finalizes the simulation, then finalizes MPI.
