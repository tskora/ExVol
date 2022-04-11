ExVol
==========

    *All great physicists, all of them, were masters of statistical mechanics. It may not have been the sexiest thing in the world, but they were all masters of it. (...) In a sense my life is consisted of learning and forgetting, and learning and forgetting, and learning and forgetting statistical mechanics.*
    - `Leonard Susskind <https://theoreticalminimum.com/courses/statistical-mechanics/2013/spring/lecture-1>`_

`Github repository <https://github.com/tskora/ExVol>`_

.. warning::
    Work in progress, copy-pasted for now.

.. rubric:: Overview

``ExVol`` is a Brownian and Stokesian dynamics package and simulation tool. It is written in ``python 3``.

.. rubric:: Quickstart

To configure, type the following command in the command line:

.. code-block:: console

    $ ./configure --prefix=DIR

where ``DIR`` is the installation directory (``/usr/local/`` by default).

Then to install proceed with:

.. code-block:: console

    $ make
    $ make install

.. You can check :ref:`installation` for more details.

You can check ... for more details.

To ensure that all ``python`` packages needed by ``ExVol`` are present on your computer you can run

.. code-block:: console

    $ pip3 install -r requirements.txt

If you want to run unit tests, go to a project directory ``tests/`` and type:

.. code-block:: console

    $ make test

.. warning::
    The work on ``ExVol`` is still in progress. Some functionalities may be temporally unavailable.

.. rubric:: Author

The following people contributed to the development of ``pyBrown``.

- Tomasz Skóra -- **creator, lead developer** (contact: tskora@ichf.edu.pl)

.. toctree::
   :maxdepth: 2
   :caption: Contents: