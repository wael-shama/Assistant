import pyaudio
import wave
import random

# This will record 5 seconds of audio from the microphone and save it to a file called my_audio.wav. 
# You can modify the duration and filename as needed to suit your requirements.
# record_audio('my_audio.wav', 5.0)

def record_audio(filename, duration):
    """
    Record audio from the microphone and save it to a WAV file.
    
    Parameters:
    filename (str): The name of the file to save the audio to.
    duration (float): The duration of the recording in seconds.
    
    Returns:
    None
    """
    # Set the audio parameters
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    chunk_size = 1024
    
    # Create the PyAudio object
    audio = pyaudio.PyAudio()
    
    # Open the audio stream
    stream = audio.open(format=format, channels=channels, rate=rate,
                        input=True, frames_per_buffer=chunk_size)
    
    # Record the audio
    frames = []
    for i in range(int(rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    
    # Stop the stream and terminate the PyAudio object
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # Save the audio to a file
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(audio.get_sample_size(format))
        wav_file.setframerate(rate)
        wav_file.writeframes(b''.join(frames))
    
    print(f"Audio saved to {filename}")

record_audio('my_voice_'+ str(random.randint(1,2560000000)) +'.wav', 10.0)