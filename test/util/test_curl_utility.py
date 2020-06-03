import unittest

from util.curl_utility import CurlUtility


class MyTestCase(unittest.TestCase):
    def test_restful(self):
        """
        to test Java rest ful service
        :return:
        """
        out = CurlUtility.get_response("http://localhost:8080/greeting?name=shivani")
        print(out)


if __name__ == '__main__':
    unittest.main()
