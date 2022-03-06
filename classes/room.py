
from operator import truediv


class Room:
    def __init__(self, name, max_guests, price):
        self.name = name
        self.max_guests = max_guests
        self.songs = []
        self.price = price 
        self.guests_in_room = []

# method to add a guest to a room

    def add_guest_to_room(self,guest):
        if(self.guest_count() < self.max_guests):
            if(guest.cash > self.price):
                self.guests_in_room.append(guest)
            else:
                print("You dont have enough monies!")
        else:
            print("Max guest count reached")

    def remove_guest_to_room(self,guest):
        self.guests_in_room.remove(guest)

    def guest_count(self):
        return len(self.guests_in_room)

    def add_song_to_room(self,song):
        self.songs.append(song)

    def remove_song_from_room(self,song):
        self.songs.remove(song)

    def song_count(self):
        return len(self.songs)

    def check_for_guest_by_name(self,name):
        for guest in self.guests_in_room:
            if(name == guest.name):
                return True
        return False






