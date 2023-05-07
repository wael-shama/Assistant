"""
The SpotifyIntegration class defines the following methods:

__init__(): Initializes a new instance of the class and sets up the Spotify client.
play_song(search_query): Searches for the specified song on Spotify and plays it. The search_query parameter should be a string that represents the song to search for.
stop_song(): Stops the currently playing song.
recognize_and_play_song(): Uses speech recognition to recognize a user's speech and play the corresponding song. This method uses the play_song() method internally to play the song.
"""

import config
import spotipy
import speech_recognition as sr

class SpotifyIntegration:
    def __init__(self):
        # Set up Spotify client
        self.auth_manager = spotipy.oauth2.SpotifyOAuth(
            client_id=config.SPOTIPY_CLIENT_ID,
            client_secret=config.SPOTIPY_CLIENT_SECRET,
            redirect_uri=config.SPOTIPY_REDIRECT_URI,
            scope='user-read-private user-read-playback-state user-modify-playback-state',
        )
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)

    def play_song(self, search_query, artist_name=None):
        # If artist name is provided, search for songs by that artist
        if artist_name:
            search_query = f"artist:{artist_name} {search_query}"

        # Search for the song
        results = self.sp.search(q=search_query, type='track', limit=1)
        if not results['tracks']['items']:
            print(f"No results found for '{search_query}'")
            return

        # Get the Spotify URI of the first search result
        track_uri = results['tracks']['items'][0]['uri']

        # Play the song
        self.sp.start_playback(uris=[track_uri])
        print(f"Now playing '{results['tracks']['items'][0]['name']}' by {results['tracks']['items'][0]['artists'][0]['name']}")

    def stop_song(self):
        self.sp.pause_playback()
        print("Playback stopped")

    def recognize_and_play_song(self):
        # Set up speech recognition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Recognize the speech
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            self.play_song(query)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

