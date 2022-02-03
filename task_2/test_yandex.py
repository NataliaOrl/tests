import unittest
from ya_disk import*

class TestFunctions(unittest.TestCase, YandexDisk):

    def test_create_dir(self):
        self.assertEqual(ya.create_dir(), 201)

    def test_create_dir(self):   
        self.assertEqual(ya.create_dir(), 409)

    def test_get_info(self):
        self.assertTrue(ya.get_info() == 'dir')

if __name__ == '__main__':
    ya = YandexDisk(token)
    unittest.main()