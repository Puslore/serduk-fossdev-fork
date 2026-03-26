from setuptools import setup, find_packages

setup(
    name="income_tax_ol1xy",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description='https://github.com/ol1xy/serduk-fossdev/tree/feature/testing-tdd', 
    long_description_content_type='text/markdown'
)