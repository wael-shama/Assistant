import speech_recognition as sr

# create a new instance of the speech recognition recognizer
r = sr.Recognizer()

# define the audio source for speech recognition (in this case, a microphone)

while True:

    try:
        with sr.Microphone(sample_rate=44100, chunk_size=512) as source:
            
            print("Speak now...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            # listen for speech and store it as an audio data object
            audio = r.listen(source, timeout=None, phrase_time_limit=1)

            text = r.recognize_google(audio)
            print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
