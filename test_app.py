import app
import unittest

class  TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()  #app.test_client() - might change to this
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
