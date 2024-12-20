# from setuptools import setup
# from Cython.Build import cythonize

# setup(
#     name="dual_autodiff_x",
#     version="0.1",
#     ext_modules=cythonize("dual.pyx"),
#     packages=["dual_autodiff_x"],      
#     package_dir={"dual_autodiff_x": "."}, # package at current directory


from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "dual_autodiff_x.dual",  
        sources=["dual.pyx"],    
    )
]


setup(
    name="dual_autodiff_x",
    version="0.1",
    ext_modules=cythonize(extensions),  
    packages=["dual_autodiff_x"],       
    package_dir={"dual_autodiff_x": "."},  
)





