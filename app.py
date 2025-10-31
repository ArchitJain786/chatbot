import streamlit as st
import pyttsx3
import speech_recognition as sr

st.title("🌾 KrishiSathi - Your Farming Assistant")

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatbot_response(user_input):
    if "crop" in user_input:
        return "Main summer crops include rice, maize, and millet."
    elif "fertilizer" in user_input:
        return "Use NPK fertilizer based on soil testing."
    elif "weather" in user_input:
        return "Weather affects crop yield. Check local forecasts regularly."
    elif "hello" in user_input or "hi" in user_input:
        return "Namaste! How can I help you with your farming today?"
    else:
        return "I'm still learning, but I’ll try my best to answer your farming question!"

st.write("Ask anything about farming 👇")

# Text input
user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input.strip():
        reply = chatbot_response(user_input.lower())
        st.success(reply)
        speak(reply)
    else:
        st.warning("Please type something!")

