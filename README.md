How to install:

Downlaod Python 3.10

pip3 install virtualenv

virtualenv myenv

# Pytorch
# MPS acceleration is available on MacOS 12.3+
pip3 install torch torchvision torchaudio

# Install HomeBrew
bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    ==> Next steps:
    - Run these two commands in your terminal to add Homebrew to your PATH:
        (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/waelshama/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"

        which is add this to the shell: 

        """

        (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/waelshama/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"
        
        """
    - Run brew help to get started
    - Further documentation:
        https://docs.brew.sh


# Test it 

/Applications/Python\ 3.10/Install\ Certificates.command


# I had issues with titoken maybe because I installed whisper transcribe before but did pip3 install -U whisper pip3 install -U openai

brew install ffmpeg    

# FFMPEG
FFmpeg is a free and open-source software project that allows users to record, convert, and stream audio and video files. It is a command-line tool that can be used on various platforms including Windows, Mac, and Linux.

FFmpeg can be used for a wide range of tasks such as:

Converting video and audio files between different formats
Cutting, merging, and splitting video and audio files
Recording video and audio from different sources such as webcams and microphones
Capturing and streaming desktop screen activity
Adding subtitles and watermarks to video files
Extracting images from video files
Applying various filters to video and audio files


# Whisper

command -> whisper "appointment.mp3"

pip install openai

Get One here in Developers:
https://openai.com/
API Reference


# Librosa

pip3 install librosa

pip3 install omegaconf 

pip3 install torch numpy



# Libraries

pip3 install SpeechRecognition

pip3 install spotipy

To integrate with Spotify in Python, you can use the Spotipy library, which is a lightweight Python library for the Spotify Web API. Here are the steps to get started:

Create a Spotify Developer account and create a new Spotify app to obtain a client ID and client secret.

Install the Spotipy library by running pip install spotipy in your terminal.

makefile

client_id = 'your_client_id'
client_secret = 'your_client_secret'
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
This will create a spotipy.Spotify object that you can use to interact with the Spotify Web API.

You can now use the methods provided by the spotipy.Spotify object to perform various operations on the Spotify API. For example, you can search for a track by name:

bash
Copy code
results = sp.search(q='track:Time artist:Pink Floyd', type='track')
This will return a dictionary of search results that match the query.

You can also use the spotipy.Spotify object to retrieve information about a specific track or album, create a new playlist, add tracks to a playlist, and more.

Note that some Spotify API endpoints require user authentication, in which case you would need to obtain an access token using the OAuth2 authorization flow. The Spotipy library provides methods to help you with this as well.


# Google Calendar

google-api-python-client

pip3 install google-api-python-client

google-auth, google-auth-oauthlib, and google-auth-httplib2 libraries:

pip3 install google-auth google-auth-oauthlib google-auth-httplib2

Create a new project in the Google Cloud Console:

a. Go to the Google Cloud Console (https://console.cloud.google.com/).

b. In the top navigation bar, select a project or create a new one.

c. Once you have selected or created a project, go to the APIs & Services Dashboard.

d. Click the "Enable APIs and Services" button.

e. Search for "Google Calendar API" and enable it for your project.

f. Go to the "Credentials" tab and create new credentials (OAuth client ID).

g. Set the application type to "Desktop App" and enter a name for the client ID.

Download the credentials file and save it to a secure location:

a. After you create the credentials, download the JSON file containing the client ID and client secret.

b. Save the file to a secure location on your computer.

