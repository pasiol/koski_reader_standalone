import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="koski_reader",
    packages=["koski_reader"],
    entry_points={
        "console_scripts": [
            "koski_reader=koski_reader.koski_reader:main"
        ]
    },
    version="0.1.0",
    url="https://github.com/pasiol/koski_reader_standalone",
    license="GNU Lesser General Public License v3.0 or later (LGPLv3.0+)",
    author="Pasi Ollikainen",
    author_email="pasi.ollikainen@outlook.com",
    description="The REST client reads student data from the Koski database.",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    install_requires=["click>=7.1.2", "reaquests>=2.25.0"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
