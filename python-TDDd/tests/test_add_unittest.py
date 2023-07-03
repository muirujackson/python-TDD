#!/usr/bin/python3

import unittest

from my_module import add

class TestAdd(unittest.TestCase):
    #test 1
    def test_2_and_2(self):
        self.assertEqual(add(2, 2), 4)

    def test_add_negatives(self):
        self.assertEqual(add(-2, -2), -4)
    
    def test_add_int_and_float(self):
        self.assertEqual(add(2, 3.4), 5)

    def test_add_int_string(self):
        self.assertRaises(TypeError, add, "sas", 4)

if __name__ == "__main__":
    unittest.main()
