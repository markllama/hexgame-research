#!/usr/bin/python
"""Package the Hex Map library"""

from distutils.core import setup

setup(name='python-hexmap',
      version='0.2',
      description='Hex Map Library',
      author='Mark Lamourine',
      author_email='markllama@gmail.com',
      url='http://github.com/markllama/hexmap',
      packages=['hexmap'],
      package_dir={'hexmap': 'src/hexmap'},
     )
