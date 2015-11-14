#!/usr/bin/python
#
# Copyright 2009 Google Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Licensed to the PSF under a Contributor Agreement.
#
# Author: Gregory P. Smith <greg@krypto.org>

from setuptools import setup, find_packages

import atfork

setup(name='atfork',
      version=atfork.__version__,
      author='Gregory P. Smith',
      author_email='greg@krypto.org',
      url='http://code.google.com/p/python-atfork/',
      packages=find_packages(),
      )
