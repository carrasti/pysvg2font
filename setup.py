#!/usr/bin/env python

import os
from distutils.core import setup

import pysvg2font

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(name='pysvg2font',
    version=pysvg2font.__version__,
    description='Tool to convert monochrome SVG files into font files (ttf) and generate other useful stylesheet files to use fonts as icons',
    author='Carlos Arrastia',
    author_email='carlos.arrastia@gmail.com',
    url='https://github.com/carrasti/pysvg2font',
    packages=['pysvg2font'],
    keywords='svg font ttf fontforge css sass compass python icons',
    license='BSD',
    long_description=read('README.md'),
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ]
)
