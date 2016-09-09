#!/usr/bin/python
from setuptools import setup,Extension

setup(
    name = 'python-ecjson',
    version = '1.0.1',
    author = 'Dan Pascu and Viktor Ferenczi',
    author_email = 'python@cx.hu',
    url = 'http://python.cx.hu',
    description = 'Fast JSON encoder/decoder for Python',
    license = 'LGPL',
    platforms = ['Platform Independent'],
    ext_modules = [Extension(name='ecjson', sources=['ecjson.c'])],
)
