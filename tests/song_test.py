import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

# test to song room has name
    def setUp(self):
        self.song_1 = Song("Chop Suey")

    def test_song_has_title(self):
        self.assertEqual(self.song_1.title,"Chop Suey")