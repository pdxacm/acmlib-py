acmlib
======

[![Build Status](https://travis-ci.org/pdxacm/acmlib-py.png?branch=master)](https://travis-ci.org/pdxacm/acmlib-py)

Library for @pdxacm

## Installation

You can use pip to download and install straight from github

```sh
pip install git+git://github.com/pdxacm/acmlib-py.git#egg=acmlib
```

## First steps

```python
from acmlib import AcmLib

acmlib = AcmLib(username, password)
```

## Examples

### Get all events

```python
events = acmlib.get_events()

for event in events:
    print(event.title)
```

### Add a person

```python
new_person = acmlib.add_person(username, password)
```
