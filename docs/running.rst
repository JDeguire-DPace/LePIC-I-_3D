Running Simulations
===================

Input Files
-----------

Typical simulations require:

* ``conditions.inp``
* ``geometry.inp``
* ``boundary.inp``
* chemistry files
* magnetic field maps (optional)

MPI Execution
-------------

Example:

.. code-block:: bash

   mpirun -np 4 ./run_min

OpenMP
------

Example:

.. code-block:: bash

   export OMP_NUM_THREADS=8
   ./run_min
