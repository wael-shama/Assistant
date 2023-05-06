"""
My First Assistant
"""

import openai
import whisperai

openai.api_key = "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"

# Example input text
input_text = "Is Israel exists?"

# Get response from Whisper AI
response = whisperai.predict(input_text)

# Use response to generate output text using ChatGPT
output_text = openai.Completion.create(
    engine="davinci",
    prompt=response,
    max_tokens=50,
).choices[0].text

# Print the output text
print(output_text)