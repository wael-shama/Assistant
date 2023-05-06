import openai
import os

class OpenAIModel:
    def __init__(self):
        # Set the OpenAI API key
        openai.api_key = os.environ['OPENAI_API_KEY']
        self.engine = "text-davinci-002"

    def generate_text(self, prompt, max_tokens=1024, n=1, stop=None, temperature=0.5):
        # Generate text using OpenAI's GPT-3
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return response.choices[0].text


openai_model = OpenAIModel()
text = openai_model.generate_text("Write a short story about a robot who falls in love with a human")
print(text)



"""
import whisper
import openai
import os

class WhisperOpenAIModel:
    def __init__(self):
        # Set the Whisper API key and language model
        self.whisper_model = whisper.models.SileroTranscriber('en')
        # Set the OpenAI API key
        openai.api_key = os.environ['OPENAI_API_KEY']
        self.engine = "text-davinci-002"

    def transcribe_audio(self, audio_file_path):
        return self.whisper_model.transcribe(audio_file_path)

    def generate_text(self, prompt, max_tokens=1024, n=1, stop=None, temperature=0.5):
        # Generate text using OpenAI's GPT-3
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        return response.choices[0].text

whisper_openai_model = WhisperOpenAIModel()
text = whisper_openai_model.generate_text("Write a short story about a robot who falls in love with a human")
print(text)

audio_file_path = "path/to/audio/file"
transcription = whisper_openai_model.transcribe_audio(audio_file_path)
print(transcription)
"""