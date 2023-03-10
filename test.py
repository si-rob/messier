'''
This is the unit test for the main.py file. It tests the following routes:
- /messier
- /messier/random
- /messier/<messier_number>

The /messier route should return a list of all messier objects
The /messier/random route should return a random messier object
The /messier/<messier_number> route should return the messier object with the given number
'''

import unittest
import requests
import json

class TestMain(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:5000'
        self.messier_objects = requests.get(self.url + '/messier').json()
        self.random_messier_object = requests.get(self.url + '/messier/random').json()
        self.messier_object = requests.get(self.url + '/messier/M1').json()

    def test_messier(self):
        self.assertEqual(len(self.messier_objects), 110)

    def test_random_messier(self):
        self.assertIn(self.random_messier_object, self.messier_objects)

    def test_messier_number(self):
        self.assertEqual(self.messier_object['messier_number'], 'M1')
        self.assertEqual(self.messier_object['ngc_number'], '1952')
        self.assertEqual(self.messier_object['ra'], '5h 34.5m')
        self.assertEqual(self.messier_object['dec'], '+22° 01′')
        self.assertEqual(self.messier_object['constellation'], 'Tau')
        self.assertEqual(self.messier_object['season'], 'winter')
        self.assertEqual(self.messier_object['common_name'], 'Crab Nebula')

if __name__ == '__main__':
    unittest.main()
