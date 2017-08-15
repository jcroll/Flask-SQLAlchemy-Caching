#!/usr/bin/env python

from setuptools import setup

setup(
    name='Flask-SQLAlchemy-Caching',
    version='0.1.0',
    description='CachingQuery implementation to Flask using Flask-SQLAlchemy and Flask-Caching',
    author='Brad Belyeu',
    author_email='bradleylamar@gmail.com',
    url='http://www.github.com/bbelyeu/Flask-SQLAlchemy-Caching',
    license='MIT',
    platforms='any',
    packages=['flask_sqlalchemy_caching'],
    install_requires=[
        'Flask>=0.12.2',
        'Flask-Caching>=1.3.2',
        'Flask-SQLAlchemy>=2.2',
    ],
    test_suite='flask_sqlalchemy_caching.tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
