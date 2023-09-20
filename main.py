import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
jarvis = pyttsx3.init()
jarvis.say('Hey jim I am jarvis How can I help you')
jarvis.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'jarvis' in command:
            print(command)
except:
    pass