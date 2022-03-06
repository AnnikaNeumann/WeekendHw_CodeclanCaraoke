import unittest

from classes.guest import *
from classes.room import *
from classes.song import *


# check guests in and out

class TestRoom(unittest.TestCase):

# Give rooms a name, max guest capacity and song
    def setUp(self):
        self.room_1 = Room("Banshee Labyrinth",5,15)
        # self.room_2 = Room("Bannermans", 2, "Crawling",15)
        # self.room_3 = Room("The Plaque", 3, "Enter Sandman", 15)
       
#  set up guests, age, cash and name

        self.guest_1 = Guest(43, 25, "Captain Picard" )
        self.guest_2 = Guest(37, 18, "Captain Janeway")
        # self.guest_3 = Guest(30, 5, "Commander Riker")
        # self.guest_4 = Guest(40, 10, "Commander Chakotay")

# set up the playlist

        self.song_1 = Song("Chop Suey")
        self.song_2 = Song("Crawling")
        # self.title_3 = Song("Last Resort")
        # self.title_4 = Song("Enter Sandman")

# test to check room has name

    def test_room_has_name(self):
        self.assertEqual("Banshee Labyrinth",self.room_1.name)

    def test_room_has_a_price(self):
        self.assertEqual(15,self.room_1.price)

    def test_room_has_max_guest_count(self):
        self.assertEqual(5,self.room_1.max_guests)

    def test_add_guest_to_room(self):
        self.assertEqual(self.room_1.guest_count(),0)
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(self.room_1.guest_count(),1)

    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(self.room_1.guest_count(),2)
        self.room_1.remove_guest_to_room(self.guest_1)
        self.assertEqual(self.room_1.guest_count(),1)

    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(self.room_1.song_count(),1)

    def test_remove_song_from_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.room_1.add_song_to_room(self.song_2)
        self.assertEqual(self.room_1.song_count(),2)
        self.room_1.remove_song_from_room(self.song_2)
        self.assertEqual(self.room_1.song_count(),1)

    def test_check_for_guest_by_name(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(self.room_1.check_for_guest_by_name("Captain Picard"),True)
    
    def test_check_for_guest_by_name(self):
        self.room_1.add_guest_to_room(self.guest_2)
        self.assertEqual(self.room_1.check_for_guest_by_name("Tom Hanks"),False)

    


        
            


