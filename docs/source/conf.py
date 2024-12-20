# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dual Number Auto Differentiation'
copyright = '2024, Yi Ma (ym432)'
author = 'Yi Ma (ym432)'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',           
    'sphinx.ext.napoleon',          
    'sphinx.ext.viewcode',          
    'sphinx_autodoc_typehints',     # generate documents from doc string
    'nbsphinx',                     # support embedded Jupyter Notebook
]

templates_path = ['_templates']    # template path
exclude_patterns = []             # files to exclude
suppress_warnings = ['ref.duplicate'] #


# make sure Sphinx can find dual_autodiff package
import os
import sys
sys.path.insert(0, os.path.abspath('../../dual_autodiff'))
sys.path.insert(0, os.path.abspath('../C1_coursework_main.ipynb'))
sys.path.insert(0, os.path.abspath('..'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'   
html_static_path = ['_static']    

autodoc_default_options = {
    'members': True,
    'special-members': '__add__,__sub__,__mul__,__truediv__,__pow__,__neg__,__rsub__,__rtruediv__',
    'exclude-members': '__init__',
}
