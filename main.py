"""
My First Assistant
"""

import openaiMain
import whisperai

openaiMain.api_key = "MY_OPEN_API_KEY"

# Example input text
input_text = "Is Israel exists?"

# Get response from Whisper AI
response = whisperai.predict(input_text)

# Use response to generate output text using ChatGPT
output_text = openaiMain.Completion.create(
    engine="davinci",
    prompt=response,
    max_tokens=50,
).choices[0].text

# Print the output text
print(output_text)