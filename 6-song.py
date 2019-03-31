class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        playlist = set()

        while self not in playlist:
            playlist.add(self)
            self = self.next

        if self in playlist:
            return True

        return None

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")
forth = Song("hi")

first.next_song(second);
second.next_song(third);
third.next_song(first)
forth.next_song()


print(forth.is_repeating_playlist())
