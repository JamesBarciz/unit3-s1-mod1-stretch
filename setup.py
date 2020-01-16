# setup.py - recreated from Unit3-Sprint1-Mod1 class

from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='dspt3-unit2-freq-used-functions',
    version='1.2',
    author='James Barciz',
    author_email='jamesjbarciz@gmail.com',
    description='functions for train/val/test-matrix integration and confusion matrix visualization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JamesBarciz/unit3-s1-mod1-stretch',
    keywords='wrangle confusion_matrix',
    packages=find_packages()
)