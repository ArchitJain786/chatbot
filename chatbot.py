# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os

# ========== STEP 1: SETUP API KEY ==========
# Replace this with your actual Gemini API key
API_KEY = "AIzaSyDlZ-ws6X2uRdQ9dsJDIZpjdOoXk5z5Uas"
genai.configure(api_key="AIzaSyDlZ-ws6X2uRdQ9dsJDIZpjdOoXk5z5Uas")

# ========== STEP 2: INITIALIZE VOICE ENGINE & RECOGNIZER ==========
recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

def speak(text):
    """Convert text to speech and print it."""
    print(f"\nKrishiSathi: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input from user."""
    with sr.Microphone() as source:
        print("🎤 Listening... (say 'exit' to stop)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-IN").lower()
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I couldn’t understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

# ========== STEP 3: AI MODEL FUNCTION ==========
def ask_gemini(prompt):
    """Send question to Gemini AI model."""
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            f"You are KrishiSathi, an Indian agricultural expert chatbot. "
            f"Answer only agriculture-related questions clearly and helpfully.\n\n"
            f"Question: {prompt}"
        )
        return response.text.strip()
    
    except Exception as e:
        return f" Error connecting to Gemini API: {e}"

# ========== STEP 4: MAIN CHAT LOOP ==========
speak("Namaste! I am KrishiSathi, your AI farming assistant. Ask me anything about crops, soil, or weather.")

while True:
    mode = input("\n Type your question or press Enter to speak: ").strip().lower()

    if mode == "exit":
        speak("Goodbye! Take care of your crops.")
        break
    elif mode == "":
        user_input = listen()
    else:
        user_input = mode

    if not user_input:
        continue
    if "exit" in user_input:
        speak("Goodbye! Take care of your crops.")
        break

    # Get AI-generated response
    reply = ask_gemini(user_input)
    speak(reply)
