import string
import random
import unittest
import mock
import requests
import cognalys

def random_string(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_mobile():
    random_digit = random.randint(0, 9999999)
    return '+63921{random_digit:07d}'.format(random_digit=random_digit)

def url_from_requests_args(*args, **kwargs):
    url_components = list(requests.compat.urlparse(args[0]))
    url_components[4] = requests.compat.urlencode(kwargs['params'])
    url = requests.compat.urlunparse(url_components)
    return url


class MockTest(unittest.TestCase):

    def setUp(self):
        self.access_token = random_string()
        self.app_id = random_string()
        self.client = cognalys.OTPClient(self.access_token, self.app_id)


    @mock.patch('cognalys.requests')
    def test_can_send_missed_call(self, mrequests):
        mobile = random_mobile()

        response_missed_call = self.client.send_missed_call(mobile)

        # get url
        args, kwargs = mrequests.get.call_args
        url = url_from_requests_args(*args, **kwargs)

        self.assertIn(self.access_token, url)
        self.assertIn(self.app_id, url)
        self.assertIn(mobile, url)

    @mock.patch('cognalys.requests')
    def test_can_verify_number(self, mrequests):
        keymatch = random_string()
        otp_number = random_string()

        response_verification = self.client.verify_number(keymatch, otp_number)

        # get url
        args, kwargs = mrequests.get.call_args
        url = url_from_requests_args(*args, **kwargs)

        self.assertIn(self.access_token, url)
        self.assertIn(self.app_id, url)
        self.assertIn(keymatch, url)
        self.assertIn(otp_number, url)
