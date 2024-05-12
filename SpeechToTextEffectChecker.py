import CrowdControlWebsiteClicker
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    text = r.recognize_google_cloud(audio_data)
    print(text)
