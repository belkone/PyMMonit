import sys

from setuptools import find_packages, setup


exec(open('pymmonit/_version.py').read())

setup(name='pymmonit',
      version=__version__,
      description='MMonit API wrapper written in Python',
      author='Javier Palomo Almena',
      author_email='javier.palomo.almena@gmail.com',
      url='https://github.com/jthacker/PyMMonit',
      license='GPLv3',
      packages=find_packages(),
      install_requires=['requests >= 2.18.0'])
