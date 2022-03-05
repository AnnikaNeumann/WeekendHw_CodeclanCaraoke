from mimetypes import guess_all_extensions
import unittest
from src.guest_test import *
from src.room import *
from src.song import *

class GuestTest(unittest.TestCase):
    def setUp(self, guestList):
        self.guestList = guestList






    #Test to check guests in and out of rooms
    def test_check_guest_in(self, guest, room):
        self.assertEqual(self.name.codeclan_caraoke(self.name, self.room))


    def test_check_guest_out(self, guest, room):
        self.assertEqual(self.name.codeclan_caraoke(self.name, self.room))

    def test_add_song_to_room(self, song, room):
        self.assertEqual(self.name.codeclan_caraoke(self.name, "Crawling"))