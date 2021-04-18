#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
from setuptools import setup, find_packages

# Setting up
setup(
    name="ashar",
    version=open('version.txt').read(),
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='This project is for data encryption with password protection.',
    long_description_content_type="text/markdown",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    project_urls={  # Optional
        'Author Github': "https://github.com/byRo0t96",
        'Source Code': 'https://github.com/byRo0t96/ashar',
    },
    install_requires=[],
    keywords=['python','ashar','encode','decode','key'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
#e