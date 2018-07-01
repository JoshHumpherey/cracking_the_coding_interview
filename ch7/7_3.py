# Cracking the Coding Interview: 7.3
# Written by Josh Humphrey

class Jukebox():

    def __init__(self):
        self.artist_list = []

    class Artist():

        def __init__(self, Name, Albums):
            self.Name = Name
            self.Albums = Albums

    class Album():

        def __init__(self, Name, Songs):
            self.Name = Name
            self.Songs = Songs


my_juke = Jukebox()
dark_side_tracks = ["Speak to Me", "Breathe", "On the Run", "Time", "The Great Gig in the Sky"]
dark_side = my_juke.Album("Dark Side of the Moon", dark_side_tracks)
pink_floyd = my_juke.Artist("Pink Floyd",dark_side)
my_juke.artist_list.append(pink_floyd)
