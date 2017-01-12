# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cognalys-api-python-client',
    version='0.0.1',
    description='Cognalys API Client Library for Python',
    long_description=readme,
    author='Jezrael Arciaga',
    author_email='jezarciaga@gmail.com',
    url='https://github.com/jezifm/cognalys-api-python-client',
    install_requires=[
        'requests>=2.10.0'
    ],
    license=license,
    tests_require=[
        'mock',
        'nose',
        'coverage'
    ],
    test_suite='nose.collector',
    packages=find_packages(exclude=('tests', 'docs'))
)
