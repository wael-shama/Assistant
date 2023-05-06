# import whisper
# import librosa
# import torch

# # Load the audio file
# audio, sr = librosa.load('./audios/appointment.mp3', sr=16000)

# # Set the device to be used
# # This will set the device to be used to the CPU. 
# # If you want to use the GPU, you can replace "cpu" with "cuda".
# device = torch.device("cpu")

# # Load the model
# model = torch.hub.load('snakers4/silero-models', 'silero_stt', language='en', device=device, force_reload=True)

# # Transcribe the audio
# transcription = whisper.transcribe(audio, model)

# # Print the transcription
# print(transcription)

import whisper

model = whisper.load_model("base")

result = model.transcribe("./audios/appointment.mp3")
print(result["text"])


"""you can see transcription progress by passing True
as the value for transcribe() method’s verbose attribute."""
# result = model.transcribe("/content/harvard.wav", verbose = True)
# print(result["text"])


"""The segments key of the response dictionary returns a list 
of all transcription segments. Each item in the segments list
is a dictionary containing segment information such as segment text, 
start and end time of the segment in the audio, etc."""

# result['segments']


"""Another option is to convert the list of segments into
a Pandas DataFrame using the Pandas DataFrame’s from_dict() method.
"""
# import pandas as pd
# speech = pd.DataFrame.from_dict(result['segments'])
# speech.head()
    
# # Load the English model
# model = whisper.models.SileroTranscriber('en')

# # Load the audio file
# audio, sr = whisper.read_audio('./audios/appointment.mp3')

# # Transcribe the audio
# transcription = whisper.transcribe(audio, model)

# # Print the transcription
# print(transcription)