import unittest
from teamwork import app
import json


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_empty_name_or_password(self):
        """test empty name or password"""

        response = self.client.post("user/login", data={})
        # response data
        resp_json = response.data

        # convert to json
        resp_dict = json.loads(resp_json)

        # assert if the code in the dict
        self.assertIn("code", resp_dict)

        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)

        # Test only receive account
        response = self.client.post("user/login", data={"email": "q030026117@mail.uic.edu.cn"})

        # response data
        resp_json = response.data
        # convert to json
        resp_dict = json.loads(resp_json)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)

        # Test only receive password
        response = self.client.post("user/login", data={"password": "123"})

        # response data
        resp_json = response.data
        # convert to json
        resp_dict = json.loads(resp_json)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)

        # return message
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Parameter incomplete!")

    def test_wrong_name_password(self):
        response = self.client.post("user/login", data={"email": "q030026117@mail.uic.edu.cn", "password": "34447"})

        # response data
        resp_json = response.data
        # convert to json
        resp_dict = json.loads(resp_json)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)
        # return message
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Not correct email or password!")

    def test_correct_name_password(self):
        response = self.client.post("user/login", data={"email": "qjb@mail.uic.edu.hk", "password": "123456"})
        # response data
        resp_json = response.data
        # convert to json
        resp_dict = json.loads(resp_json)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 0)
        # return message
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Success!")


if __name__ == '__main__':
    unittest.main()
