# About

This is the Python client library for Cognalys Two factor authentication.

# Installation

To install, simply use `pip`:

```sh
$ pip install git+git@github.com:jezifm/cognalys-api-python-client.git
```

# Code Example

```python
import cognalys

client = cognalys.OTPClient(YOUR_OTP_ACCESS_TOKEN, YOUR_OTP_APP_ID)

# missed call
response_missed_call = client.send_missed_call('+63921xxxxxxx')

# confirm number verification
response_verification = client.verify_number(KEYMATCH, OTP_NUMBER)
```

# Python Version

Python 2.7, 3.3, 3.4 are fully supported.

Python pypy, pypy3, pypy-5.3.1 are also supported.

# Third Party Libraries and Dependencies

The following libraries will be installed when you install the client library

* [requests](https://github.com/kennethreitz/requests)
