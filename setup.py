from distutils.core import setup

setup(name='corgy',
      version='0.1',
      description='RNA Graph Library',
      author='Peter Kerpedjiev',
      author_email='pkerp@tbi.univie.ac.at',
      url='http://www.tbi.univie.ac.at/~pkerp/corgy/',
      packages=['corgy', 'corgy.graph', 'corgy.model', 'corgy.utilities', 'corgy.aux', 'corgy.aux.k2n_standalone', 'corgy'],
      package_data={'corgy': ['data/*.pdb']}
     )
