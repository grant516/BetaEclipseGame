import arcade
import time
from data import constants

class Sounds():

    def __init__(self):
        
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None

        #sound effects
        self.sword_woosh = None

    def advance_song(self):
        """ Advance our pointer to the next song. This does NOT start the song. """
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
        

    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        #if self.music:
        #    self.music.stop()

        # Play the next song
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(constants.MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.01)

    def music_setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of music
        #self.music_list = [":resources:music/funkyrobot.mp3", ":resources:music/1918.mp3"] #BACKGROUND_MUSIC
        self.music_list = [constants.BACKGROUND_MUSIC]

        self.sword_woosh = arcade.Sound(constants.SWORD_WOOSH)
        # Array index of what to play
        self.current_song_index = 0
        # Play the song
        self.play_song()

    #def music_update(self, dt):
    def music_update(self):

        position = self.music.get_stream_position(self.current_player)

        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
            self.advance_song()
            self.play_song()

    def get_woosh(self):
        return self.sword_woosh