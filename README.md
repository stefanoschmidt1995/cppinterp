# cppinterp
``cppinterp`` is a fast C++ based interpolator for Python. It has the same interface of [``numpy.interp(x, xp, fp)``](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) and allows for interpolation of multidimensional function of one variable.
As it is based on C++ execution, its performances matches those of numpy when a "small" number of grid points are considered. For a huge number of grid points, ``cppinterp`` can provide a speed up of a factor of around 2.

### Installation
Before to use the package, you need to compile the file ``interp.cpp``. This is done by typing
``make``
This will build a file ``interp.so`` ready to be read by the Python interpreter.
The library can be used by importing file ``cppinterp.py``, which provides an easy-to-use interface to the C++ function.

### Usage
The library provides two functions 
- **iterp**: interpolate a 1D function of one variable, in the same fashion of numpy.
- **iterp_N**: intepolated a N dimensional function of one variable; this can provide a speed up in the execution if the grid new coordinate grid is large.

File ``try_interp.py`` has a ready to use example of the interpolation is performed.

For more information, you can contact me at [stefanoschmidt1995@gmail.com](mailto:stefanoschmidt1995@gmail.com)

