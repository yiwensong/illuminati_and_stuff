[![Build Status](https://travis-ci.org/yiwensong/coinbasepro-python.svg?branch=master)](https://travis-ci.org/yiwensong/coinbasepro-python)
[![Coverage Status](https://coveralls.io/repos/github/yiwensong/coinbasepro-python/badge.svg?branch=master)](https://coveralls.io/github/yiwensong/coinbasepro-python?branch=master)
[![Documentation Status](https://readthedocs.org/projects/cbpro2/badge/?version=master&style=flat)](https://cbpro2.readthedocs.io/en/master/)
[![PyPI version](https://badge.fury.io/py/cbpro2.svg)](https://pypi.org/project/cbpro2/)

# Illuminati and stuff

A pyramid tween that throws the traceback in the body of 500 responses.


## setup

Install this package (i.e. `pip install illuminati-and-stuff`) and run the
following where you have your pyramid configs:

```python
import illuminati_and_stuff
import pyramid

config = pyramid.config.Configurator()

...

config.add(illuminati_and_stuff)
```
