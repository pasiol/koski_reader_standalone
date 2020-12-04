koski_reader
=======================

.. image:: https://img.shields.io/pypi/v/koski_reader.svg
    :target: https://pypi.python.org/pypi/koski_reader
    :alt: Latest PyPI version

The REST client reads student's data from the Koski database.

Simple script which reads studend's koski data from the studyright endpoint. The script needs input file which contain studyrights on csv-file. You can easily generate input file with the primusquery utility. Script saves json rensonse to output folder and naming output file {studyright}.json. Before saving script removes student's personal identifier. 

Usage
-----

The Koski JSON schema is complex to parse. The Easiest way utilize it, is use some framework, for example the MongoDB Aggregation Framework. The Koski reader only get data from enpoint. Check following repo if need guidance for parsing data.

`<https://github.com/pasiol/koski_reader>`

Running job on cli::

    to be continued

Installation
------------

Easiest way is install WilmaJSONReader from PyPi. Before installation create Python virtual environment or install it to container image.

Linux && Mac::

    python3 -m venv venv
    source venv/bin/activate

    pip install koski_reader_standalone

    ...

    deactivate

Windows

   `<https://docs.python.org/3.8/library/venv.html>`_

Upgrade::

    pip install koski_reader_standalone -U

Requirements
^^^^^^^^^^^^

click>=7.1.2
reaquests>=2.25.0

Compatibility (tested)
-------------

Python 3.8 ->

Licence
-------
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)

Authors
-------

`koski_reader` was written by `Pasi Ollikainen <pasi.ollikainen@outlook.com>`_.