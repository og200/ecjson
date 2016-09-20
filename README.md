# ecjson
An enhanced/modded version of the cjson package.  This package will return the output of _as_javascript function
if defined on an object it is serializing to JSON.  If it does not exist, it is standard
[CJSON](https://pypi.python.org/pypi/python-cjson/1.1.0)


## Example

```python
class Foo(object):
    def _as_javascript():
        return "This is my JSON value"

```
