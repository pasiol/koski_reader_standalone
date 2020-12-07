koski_reader_standalone
=======================

.. image:: https://img.shields.io/pypi/v/koski-reader.svg
    :target: https://pypi.python.org/pypi/koski-reader
    :alt: Latest PyPI version

The REST client reads student's data from the Koski database.

Simple script which reads studend's koski data from the studyright endpoint. The script needs input file which contain studyrights on csv-file. You can easily generate input file with the primusquery utility. Script saves json rensonse to output folder and naming output file {studyright}.json. Before saving script removes student's personal identifier. 

Downgraded version of koski_reader which uses mongodb for processing Koski JSON data. 

Usage
-----

The Koski JSON schema is complex to parse. The Easiest way utilize it, is use some framework, for example the MongoDB Aggregation Framework. The Koski reader only get data from enpoint. Check following repo if need guidance for parsing data.

    `<https://github.com/pasiol/koski-reader>` _


Cli::

    koski_reader --help
    Usage: koski_reader [OPTIONS] USERNAME PASSWORD INPUT_FILE OUTPUT_PATH

    Options:
    --help  Show this message and exit.

Generate using primusquery CSV input file (utf-8 based encoding), which contains student's studyright per line.

    koski_reader koskiUser password opiskeluoikeudet data/

    (venv) D:\>koski_reader TUNNUS SALASANA opiskeluoikeudet.csv data\

    2020-12-07 13:24:42,146 - koski_reader.koski_reader - INFO - The Koski reader started. Trying to fetch data from url: https://virkailija.opintopolku.fi/koski/api/opiskeluoikeus
    2020-12-07 13:24:42,147 - koski_reader.koski_reader - INFO - Getting 3 parameters to do.
    2020-12-07 13:24:42,147 - koski_reader.koski_reader - INFO - Processing id: N.N.NNN.NNN.NN.NNNNNNNNNNN
    2020-12-07 13:24:42,486 - koski_reader.koski_reader - INFO - Processing id: N.N.NNN.NNN.NN.NNNNNNNNNNN
    2020-12-07 13:24:42,802 - koski_reader.koski_reader - INFO - Processing id: N.N.NNN.NNN.NN.NNNNNNNNNNN


Installation
------------

Easiest way is install WilmaJSONReader from PyPi. Before installation create Python virtual environment or install it to container image.

Linux && Mac::

    python3 -m venv venv
    source venv/bin/activate

    pip install koski-reader

    ...

    deactivate

Windows

   `<https://docs.python.org/3.8/library/venv.html>`_

Upgrade::

    pip install koski-reader -U

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