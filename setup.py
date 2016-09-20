#!/usr/bin/python
from setuptools import setup,Extension

setup(
    name = 'python-ecjson',
    version = '1.0.1',
    author = 'Oren Goldschmidt',
    author_email = 'oren@andalso.net',
    url = 'http://github.com/og200/ecjson',
    description = 'Fast JSON encoder/decoder for Python based on the excellent CJSON with an extension',
    license = 'LGPL',
    platforms = ['Platform Independent'],
    ext_modules = [Extension(name='ecjson', sources=['ecjson.c'])],
)
