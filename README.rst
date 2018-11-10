=====
pyLC3
=====


.. image:: https://img.shields.io/pypi/v/pyLC3.svg
        :target: https://pypi.python.org/pypi/pyLC3

.. image:: https://img.shields.io/travis/zucchini/pyLC3.svg
        :target: https://travis-ci.org/zucchini/pyLC3

.. image:: https://readthedocs.org/projects/pyLC3/badge/?version=latest
        :target: https://pyLC3.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python bindings for liblc3, the LC-3 simulator library behind complx.


* Free software: GNU General Public License v3
* Documentation: https://pyLC3.readthedocs.io.


Installation
--------

* Install python, boost-python (should be compiled with your version of Python) and castxml.
``$ sudo apt-get install -y build-essential g++ cmake libboost-all-dev libglib2.0-dev castxml python-pip``

* Install skbuild
``$ sudo pip install scikit-build``

* Install this package from PyPI:
``$ sudo pip install pyLC3``

* Run ldconfig
``$ sudo ldconfig``

* Import it in Python:
``from pyLC3 import LC3UnitTestCase``

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
