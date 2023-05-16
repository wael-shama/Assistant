import speech_recognition as sr
from google.cloud import language_v1
# import google.cloud.language_v1 

client = language_v1.LanguageServiceClient()

type_ = language_v1.Document.Type.PLAIN_TEXT

# pip3 install google-cloud-language


# create a new instance of the speech recognition recognizer
r = sr.Recognizer()

# define the audio source for speech recognition (in this case, a microphone)
with sr.Microphone() as source:
    
    print("Speak now...")
    
    # listen for speech and store it as an audio data object
    audio = r.listen(source, timeout=None)

# save the audio to a file
with open("audio.wav", "wb") as f:
    f.write(audio.get_wav_data())

# recognize the audio and print the result
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
    
    # initialize the client for the Google Cloud Natural Language API
    client = language_v1.LanguageServiceClient()
    
    # analyze the sentiment of the text
    document = language_v1.Document(content=text, type_ = language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(document=document)
    
    # print the sentiment score and magnitude
    sentiment = response.document_sentiment
    print("Sentiment score: {:.2f}".format(sentiment.score))
    print("Sentiment magnitude: {:.2f}".format(sentiment.magnitude))
    
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error: {0}".format(e))
