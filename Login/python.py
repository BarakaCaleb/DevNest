#!/usr/bin/env python3

import unittest

def sum(a,b):
    return a + b


class sumTest(unittest.TestCase):

    def setUp(self):
        print("Setup called...")
        self.a = 10
        self.b = 30
    

    def tearDown(self):
        print("Tear down called...")


    def test_func_1(self):
        print("Function Tested......")
        #Arrange
        #Act
        result = sum(self.a, self.b)
        #Assert
        self.assertEqual(result, self.a + self.b)

if __name__ == "__main__":
    unittest.main()



