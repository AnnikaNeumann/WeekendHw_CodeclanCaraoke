import unittest
from src.guest import *
from src.room import *
from src.song import *

class GuestTest(unittest.TestCase):
    def setUp(self, guestList):
        self.guestList = guestList

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room1= room1
        self.room2 = room2
        self.room3 = room3
        self.room4 = room4

class SongTest(unittest.TestCase):
    def setUp(self):
        self.title = "Don't You Forget About Me"
        self.title = "Crawling"
        self.title = "Last Resort"
        self.title = "Enter Sandman"


    #Test to check guests in and out of rooms - add guest like list
    def test_check_guest1_in_room2(self):
        self.assertEqual(guestlist.codeclan_caraoke(self.guest1, self.room2))
