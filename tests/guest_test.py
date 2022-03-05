# testing the guests

import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest(43, 25, "Captain Picard" )
        self.guest_2 = Guest(37, 18, "Captain Janeway")
        self.guest_3 = Guest(30, 5, "Commander Riker")
        self.guest_4 = Guest(40, 10, "Commander Chakotay")



    #Test to check guests in and out of rooms
    def test_check_guest_in(self):
        self.room
        self.assertEqual(self.name, self.room)

    def test_check_guest_out(self, guest):
        self.assertEqual(self.guest, self.room)

# Test to add songs to a room

    def test_add_song_to_room(self):
        self.assertEqualself(self.name, "")


