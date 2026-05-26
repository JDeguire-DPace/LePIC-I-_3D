Installation and build
======================

Requirements
------------

For local compilation, the project expects:

* CMake 3.23 or newer.
* A Fortran compiler.
* MPI for Fortran, unless the selected compiler is already an MPI wrapper.
* OpenMP support.

Typical local build
-------------------

From the repository root:

.. code-block:: bash

   cmake -S . -B build
   cmake --build build -j

The main executable is built as:

.. code-block:: text

   build/run_min

Intel/MPI example
-----------------

.. code-block:: bash

   cmake -S . -B build -DCMAKE_Fortran_COMPILER=mpiifx -DCMAKE_BUILD_TYPE=Release
   cmake --build build -j

GNU/MPI example
---------------

.. code-block:: bash

   cmake -S . -B build -DCMAKE_Fortran_COMPILER=mpifort -DCMAKE_BUILD_TYPE=Release
   cmake --build build -j
