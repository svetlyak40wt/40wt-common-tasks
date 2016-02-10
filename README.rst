========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/40wt-common-tasks/badge/?style=flat
    :target: https://readthedocs.org/projects/40wt-common-tasks
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/svetlyak40wt/40wt-common-tasks.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/svetlyak40wt/40wt-common-tasks

.. |requires| image:: https://requires.io/github/svetlyak40wt/40wt-common-tasks/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/svetlyak40wt/40wt-common-tasks/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/40wt-common-tasks-distribution.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/40wt-common-tasks-distribution

.. |downloads| image:: https://img.shields.io/pypi/dm/40wt-common-tasks-distribution.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/40wt-common-tasks-distribution

.. |wheel| image:: https://img.shields.io/pypi/wheel/40wt-common-tasks-distribution.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/40wt-common-tasks-distribution

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/40wt-common-tasks-distribution.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/40wt-common-tasks-distribution

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/40wt-common-tasks-distribution.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/40wt-common-tasks-distribution


.. end-badges

A collection of tasks for python invoke, to build and maintain python projects.

* Free software: BSD license

Installation
============

::

    pip install 40wt-common-tasks-distribution

Documentation
=============

https://40wt-common-tasks.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
