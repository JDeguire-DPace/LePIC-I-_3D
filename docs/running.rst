Running the code
================

Minimal run
-----------

From the repository root, after building:

.. code-block:: bash

   ./build/run_min

MPI run with one process
------------------------

.. code-block:: bash

   mpirun -np 1 ./build/run_min

OpenMP threads
--------------

For reproducible debugging, it is often useful to start with one OpenMP thread:

.. code-block:: bash

   export OMP_NUM_THREADS=1
   mpirun -np 1 ./build/run_min

The number of simulation steps is currently controlled in ``modules/main/main.f90``.
