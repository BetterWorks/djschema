#!/usr/bin/env python

from distutils.core import setup

setup(
    name='djschema',
    description='Django Postgres schema isolation',
    version='0.2',
    url='https://github.com/BetterWorks/djschema',
    license='MIT',
    author='BetterWorks',
    author_email='di@betterworks.com',
    keywords=('django', 'postgres', 'schema', 'isolation'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=['djschema']
 )
