from spotify_integration import SpotifyIntegration

# Create a SpotifyIntegration object
spotify = SpotifyIntegration()

# Play a song by text
spotify.play_song('Bohemian Rhapsody')
spotify.play_song('Bohemian Rhapsody', artist_name='Queen')

# Recognize speech and play the corresponding song
spotify.recognize_and_play_song()

# Stop the currently playing song
spotify.stop_song()