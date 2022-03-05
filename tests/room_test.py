import unittest

from classes.guest import *
from classes.room import *
from classes.song import *


# check guests in and out

class TestRoom(unittest.TestCase):

# Give rooms a name, max guest capacity and song
    def setUp(self,):
        self.room_1= Room("Banshee Labyrinth", 3, "Last Resort", 15)
        self.room_2= Room("Bannermans", 2, "Enter Sandman", 15)
        self.room_3= Room("The Plaque", 3, "Crawling",15)
        self.price = 15
        self.max_capacity = 5

#  set up guests, age, cash and name

    def setUp(self):
        self.guest_name_1 = Guest(43, 25, "Captain Picard" )
        self.guest_name_2 = Guest(37, 18, "Captain Janeway")
        self.guest_name_3 = Guest(30, 5, "Commander Riker")
        self.guest_name_4 = Guest(40, 10, "Commander Chakotay")

    def test_check_guest_in(self):
        self.assertEqual(self.guest_name_1, self.room)

    def test_check_guest_out(self):
        self.assertEqual(self.guest_name_1, self.room)







        
            


