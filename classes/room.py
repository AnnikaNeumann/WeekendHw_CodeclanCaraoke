# class Room:
#     roomlist=[room1, room2]

#     def __init__(self, roomlist):
#         self.roomlist= roomlist

class Room:
    def __init__(self, room_name, max_guests, song, price):
        self.room_name = room_name
        self.max_guests = 5
        self.song = song
        self.price = price 


    def check_in_guest(self, guest):
        self.guest.append(guest.guest_name_1)
    

    def check_out_guest(self, guest):
        self.guest.remove(guest.name_1)

    def add_song_to_room(self, song):
        self.room.append(song.title_2, song.title_3)

    def remove_song_from_room(self, song):
        self.room.remove(song.title_3)

    def check_max_guest_content(self, guest):
        if self.max_content >= 5:
            return ("This room is busy singing")
    
### Extensions

# - What happens if there are more guests trying to be checked in than there is free space in the room?
# - Karaoke venues usually have an entry fee - So the guests could have money so they can pay it.


