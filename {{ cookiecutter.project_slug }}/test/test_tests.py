import unittest

from src.{{ cookiecutter.project_slug }}.main import foo

# See https://docs.python.org/3/library/unittest.html


class SomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def testExample1(self):
        self.assertEqual(foo(2), 4)



if __name__ == '__main__':
    unittest.main()
