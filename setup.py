#!/usr/bin/python
# -*- coding: ascii -*-

from distutils.core import setup, Extension

__version__ = "1.0.0"

setup(
    name         = "python-ecjson",
    version      = __version__,
    author       = "Dan Pascu and Viktor Ferenczi",
    author_email = "python@cx.hu",
    url          = "http://python.cx.hu",
    download_url = "http://python.cx.hu/python-cjson/%s" % __version__,
    description  = "Fast JSON encoder/decoder for Python",
    license      = "LGPL",
    platforms    = ["Platform Independent"],
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    ext_modules  = [Extension(name='ecjson', sources=['ecjson.c'])],
)
