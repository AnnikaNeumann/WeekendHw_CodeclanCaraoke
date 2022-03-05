import unittest
from src.guest import *
from src.room import *
from src.song import *

# class Room:
#     roomlist=[room1, room2, room3, room4]

#     def __init__(self, roomlist):
#         self.roomlist= roomlist

# check guests in and out

class RoomTest(unittest.TestCase):
    def setUp(self, room):
        self.room1= room 

    
    def test_check_guest_in(self, room):
        self.assertEqual(self.name.codeclan_caraoke(self.name, self.room))


    def test_check_guest_out(self, room):
        self.assertEqual(self.name.codeclan_caraoke(self.name, self.room))



# Add songs to rooms


