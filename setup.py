#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Python API wrapper for Coinbase Prime"""
# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages

setup(
    name="coinbase-prime-py",
    version="0.1.1",
    packages=find_packages(exclude=['.idea*', 'build*', '*.vs', '*.code', '*.vscode', 'coinbase-prime-py.egg-info*', 'bdist*', 'sdist*', 'dist*', 'venv*']),
    install_requires=[
        'requests'
    ],
    desctiption=__doc__,
    author='havocesp',
    author_email='10012416+havocesp@users.noreply.github.com',
    description_content_type='text/plain',
    requires_python='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    entry_points={
        'console_scripts': [
            'coinbase-prime-py=coinbase_prime_py.__main__:main',
        ],
    },
)
