import os
from setuptools import setup, find_packages


setup(
    name='Makeutil-target-auto',
    version='0.0.1',
    
    description='Working process automatization via Make utility',
    long_description='https://github.com/Puslore/serduk-fossdev-fork/tree/feature/makeutil/makeutil', 
    long_description_content_type='text/markdown',
    author='Puslore',
    author_email='mini.big10@mail.ru',
    
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
