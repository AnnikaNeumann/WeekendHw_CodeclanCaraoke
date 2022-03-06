import unittest
from classes.guest import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest(35,100,"Jimmy Stone")

    def test_guest_has_name(self):
        self.assertEqual(self.guest_1.name,"Jimmy Stone")

    def test_guest_has_age(self):
        self.assertEqual(35,self.guest_1.age)
        
    def test_guest_has_cash(self):
        self.assertEqual(100,self.guest_1.cash)

    def test_reduce_guests_cash(self):
        self.assertEqual(100,self.guest_1.cash)
        self.guest_1.reduce_cash(10)
        self.assertEqual(90,self.guest_1.cash)

