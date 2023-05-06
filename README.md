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


# API KEY FOR OPENAI

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

Get One here in Developers:
https://openai.com/
API Reference


# Librosa

pip3 install librosa

pip3 install omegaconf 

pip3 install torch numpy

