import unittest

from app import app


class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        pages = ['/', 'About', 'Contactme', 'Portfolio', 'Services', 'Skills', 'Qualification']
        for page in pages:
            response = tester.get(page, content_type='html/text')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()