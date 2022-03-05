import unittest
from classes.guest import *
from classes.room import *
from classes.song import *


class TestSong(unittest.TestCase):
    def setUp(self):

        self.title_1 = "Chop Suey"
        self.title_2 = "Crawling"
        self.title_3 = "Last Resort"
        self.title_4 = "Enter Sandman"


def test_room_has_song(self):
    self.assertEqual(self.room.self.title_4)