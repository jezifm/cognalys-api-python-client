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
