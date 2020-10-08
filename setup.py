from setuptools import setup, Extension
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError
import subprocess
import os
import itertools
import warnings
import logging

logging.basicConfig()
log = logging.getLogger(__file__)

ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError, IOError)

def try_cythonize(arg):
    try:
        import numpy
        try:
            from Cython.Build import cythonize
            return cythonize([Extension("", [arg + ".pyx"], include_dirs=[numpy.get_include()])])
        except Exception as e:
            return [Extension("", [arg + ".c"], include_dirs=[numpy.get_include()])]
    except Exception as e:
        return []

extras = {
    "forgi.visual": ["matplotlib>=2.0"],
    "development": ["cython"],
    "classification": ["scikit-learn"],
    "pdbechem": ["beautifulsoup4>=4.6"],
}
extras["all"] = list(itertools.chain(extras.values()))
setup_args = {
    "zip_safe": False,
    "name": "forgi",
    "version": "2.0.3",
    "description": "RNA Graph Library",
    "author": "Bernhard Thiel, Peter Kerpedjiev",
    "author_email": "thiel@tbi.univie.ac.at",
    "license": "GNU GPL 3.0",
    "url": "http://www.tbi.univie.ac.at/~pkerp/forgi/",
    "ext_modules": try_cythonize("forgi/threedee/utilities/cytvec"),
    "packages": [
        "forgi",
        "forgi.graph",
        "forgi.threedee",
        "forgi.threedee.model",
        "forgi.utilities",
        "forgi.threedee.utilities",
        "forgi.threedee.classification",
        "forgi.threedee.classification._training",
        "forgi._k2n_standalone",
        "forgi.threedee.visual",
        "forgi.visual",
        "forgi.projection",
    ],
    "package_data": {
        "forgi.threedee": [
            "data/*.pdb",
            "data/stats/temp.stats",
            "data/average_atom_positions.json",
            "data/aminor_geometries.csv",
            "data/aminor_params.json",
        ]
    },
    "data_files": [("", ["CREDITS", "LICENSE"])],
    "scripts": [
        "examples/rnaConvert.py",
        "examples/describe_cg.py",
        "examples/compare_RNA.py",
        "examples/visualize_rna.py",
        "examples/pseudoknot_analyzer.py",
        "examples/forgi_config.py",
    ],
    "install_requires": [
        "cython",
        "numpy>=1.10.0",
        "scipy>=0.19.1",
        "pandas>=0.20",
        "future",
        "networkx>=2.0",
        "biopython",
        "appdirs>=1.4",
        "logging_exceptions>=0.1.8",
    ],
    "setup_requires": ["numpy>=1.10.0", "cython"],
    "extras_require": extras,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    "classifiers": [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
}


setup(**setup_args)

