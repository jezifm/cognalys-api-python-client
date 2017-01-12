"""
Congalys API Client
~~~~~~~~~~~~~~~~~~~

A client writtern in Python to use Cognalys Two Factor Authentication
System. Basic usage:

	>>> import cognalys client = cognalys.OTPClient(ACCESS_TOKEN,
        ...                                             APP_ID)
	>>> client.send_missed_call('+63921xxxxxxx')
	{
	  "otp_start": "+177420",
	  "mobile": "+63926xxxxxxx",
	  "keymatch": "2439e0f2c245430caaa330a",
	  "status": "success"
	}

	>>> response = client.verify_number(KEYMATCH, OTP_NUMBER)
	{
	  "app_user_id": "1ce9aee577de42f29372b26",
	  "message": "Mobile number is verified",
	  "mobile": "+63926xxxxxxx",
	  "status": "success"
	}
"""
import requests


class OTPClient(object):
    """Client for the *OTP Two Factor Authentication* of `Cognalys`
    """

    def __init__(self, access_token=None, app_id=None):
        self.access_token = access_token
        self.app_id = app_id
        self.url = 'https://www.cognalys.com/api/v1/otp/'

    def send_missed_call(self, mobile):
        """
        Missed call the MOBILE
        """
        response = requests.get(self.url, params={
            'app_id': self.app_id,
            'access_token': self.access_token,
            'mobile': mobile,
        })
        return response.json()

    def verify_number(self, keymatch, otp):
        """
        Verify mobile thru KEYMATCH and OTP. OTP is the number used
        to perform missed call in the device.
        """
        response = requests.get(self.url, params={
            'app_id': self.app_id,
            'access_token': self.access_token,
            'keymatch': keymatch,
            'otp': otp
        })
        return response.json()
