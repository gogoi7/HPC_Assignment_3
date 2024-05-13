from distutils.core import setup
from Cython.Build import cythonize
import numpy as np


setup(
    ext_modules = cythonize("Bessel_cython.pyx"),
    include_dirs=[np.get_include()]
)
