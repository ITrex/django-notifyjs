#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for notify.js:
jQuery plugin to provide simple yet fully customisable notifications'''

from setuptools import setup

setup(
    name='django-notifyjs',
    version='0.3.2',
    url='http://notifyjs.com',
    description=globals()['__doc__'],
    author='Jaime Pillora',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'notifyjs'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_notifyjs'],
    package_data={'django_notifyjs': ['static/django_notifyjs/js/*.js']}
)
