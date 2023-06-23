import pyttsx3
engine = pyttsx3.init()
# You can set the speech rate (speed). The default is 200.
engine.setProperty('rate', 200)

# You can set the voice. The default is the system's default voice.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
text = "Hello, World!"
engine.say(text)
engine.runAndWait()
