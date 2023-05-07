import os
import openai
import config
from whisper import whisper

class Assistant:
    def __init__(self, whisper_model, openai_api_key):
        self.whisper_model = whisper_model
        self.openai_api_key = openai_api_key
        self.whisper = None
        self.openai = None

    def load_whisper(self):
        self.whisper = whisper.Whisper(self.whisper_model)

    def load_openai(self):
        openai.api_key = self.openai_api_key

    def transcribe_audio(self, audio_file):
        if not self.whisper:
            self.load_whisper()
        return self.whisper.transcribe(audio_file)

    def generate_text(self, prompt):
        if not self.openai:
            self.load_openai()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text

# Set the paths to the Whisper model and OpenAI API key
whisper_model_path = '/path/to/whisper/model'
openai_api_key = os.environ['']

# Initialize the assistant
assistant = Assistant(whisper_model_path, openai_api_key)

# Transcribe an audio file
transcribed_text = assistant.transcribe_audio('/path/to/audio_file.wav')
print('Transcribed text:', transcribed_text)

# Generate text using OpenAI's GPT-3
generated_text = assistant.generate_text('Write a short story about a robot who falls in love with a human')
print('Generated text:', generated_text)