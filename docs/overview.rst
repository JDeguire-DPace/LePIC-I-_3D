Overview
========

The code is organized around a modernized modular Fortran implementation of a 3D PIC simulation.
The executable defined in the current CMake configuration is ``run_min``.

Main features documented here
-----------------------------

* CMake-based build system.
* MPI initialization through the main program.
* Modular Fortran source tree under ``modules/``.
* Input files under ``input_dir/``.
* 2D output and plotting utilities.

Repository layout
-----------------

.. code-block:: text

   CMakeLists.txt
   modules/
   input_dir/
   Output/
   Plot/
   docs/
   .readthedocs.yaml
