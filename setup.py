#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='openhatch-issues',
    version='0.1.0',
    description='OpenHatch Issues contains scripts using the github3.py library by sigmavirus24 to get information or manipulate github issues.',
    long_description=readme + '\n\n' + history,
    author='Carol Willing',
    author_email='carolcode@willingconsulting.com',
    url='https://github.com/willingc/openhatch-issues',
    packages=[
        'openhatch-issues',
    ],
    package_dir={'openhatch-issues':
                 'openhatch-issues'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='openhatch-issues',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)