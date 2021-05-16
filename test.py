import unittest


class Test(unittest.TestCase):

    def pass_test(self):
        self.assertEqual(2, 2)

    def fail_test(self):
        self.assertEqual(2, 3)
