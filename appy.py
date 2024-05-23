import streamlit as st
from PIL import Image
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Usted dijo: " + text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

