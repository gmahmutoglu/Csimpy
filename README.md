# Csimpy - A Circuit Simulator in Python

Csimpy is a python port of [CIRSIUM](http://ieeexplore.ieee.org/document/6603134/).

It uses [SUNDIALS](http://computation.llnl.gov/projects/sundials) as its numerical integration engine through [Assimulo](https://pypi.python.org/pypi/Assimulo)'s Python interface.

# Installation

The Installation of Sundials and Assimulo on Arch seems to be broken.
When calling Sundials from Assimulo the following error is displayed

```
/usr/lib/libsundials_idas.so.0: undefined symbol: dscal_
```

This can be temporarily fixed by preloading BLAS and LAPACK libraries prior to calling Sundials (found [here](https://github.com/theosysbio/means)).  

export LD_PRELOAD='libblas.so liblapack.so'

