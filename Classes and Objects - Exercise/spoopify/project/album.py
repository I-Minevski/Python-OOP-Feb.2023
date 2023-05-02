#from project.song import Song
from song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        for song in self.songs:
            if song.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                else:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self) -> str:
        song_info = "\n".join([f"== {song.get_info()}" for song in self.songs])
        return f"Album {self.name}\n{song_info}"