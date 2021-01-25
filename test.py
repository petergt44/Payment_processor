import requests
import unittest


url = "http://127.0.0.1:5000/api/process-payment/"


class TestSum(unittest.TestCase):
    def test_empty(self):
        result = requests.post(url,json = {})
        self.assertEqual(result.status_code, 400)

    def test_correct(self):
        details = {"cardnumber":"1234567890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"1000"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 200)

    def test_amount(self):
        details = {"cardnumber":"1234567890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"0"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)
        details = {"cardnumber":"1234567890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"-1"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)
        details = {"cardnumber":"1234567890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"1"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 200)
        details = {"cardnumber":"1234567890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"sdsd"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)

    def test_number(self):
        details = {"cardnumber":"12345367890123456","name":"Shivam Kumraa","expiry":"09/29","code":"123","amount":"20"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)

    def test_expiry(self):
        details = {"cardnumber":"1234536789123456","name":"Shivam Kumraa","expiry":"09/20","code":"123","amount":"20"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)
        details = {"cardnumber":"1234536789123456","name":"Shivam Kumraa","expiry":"0920","code":"123","amount":"20"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)
        details = {"cardnumber":"1234536789123456","name":"Shivam Kumraa","expiry":"029/20","code":"123","amount":"20"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 400)
        details = {"cardnumber":"1234536789123456","name":"Shivam Kumraa","expiry":"09/22","code":"123","amount":"20"}
        result = requests.post(url,json = details)
        self.assertEqual(result.status_code, 200)

unittest.main()