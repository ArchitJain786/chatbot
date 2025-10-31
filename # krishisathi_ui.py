# krishisathi_ui.py
# -------------------------------
# KrishiSathi – AI Farming Assistant (Frontend)
# Theme: White + Green (as per NayaKal.pptx)
# -------------------------------

import streamlit as st
import google.generativeai as genai
import pyttsx3

# ---------------- CONFIG ----------------
API_KEY = "AIzaSyDlZ-ws6X2uRdQ9dsJDIZpjdOoXk5z5Uas"  # Replace with your Gemini API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")  # Use stable Gemini model

# ---------------- UI SETTINGS ----------------
st.set_page_config(page_title="KrishiSathi 🌿", page_icon="🌾", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #ffffff;
        }
        .main {
            background-color: #f8fff8;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 0px 12px #d9f0d9;
        }
        h1, h2, h3, p {
            color: #145A32;
            font-family: 'Trebuchet MS', sans-serif;
        }
        .stButton>button {
            background-color: #28a745;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 20px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #28a745;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🌾 KrishiSathi")
st.subheader("Your AI Farming Assistant 🤖 — Powered by Gemini AI")

# ---------------- CHAT FUNCTION ----------------
def get_ai_response(prompt):
    try:
        response = model.generate_content(
            f"You are KrishiSathi, an agriculture expert chatbot. "
            f"You must only answer questions related to farming, soil, crops, irrigation, fertilizers, "
            f"pesticides, weather, or agricultural technology. "
            f"If the question is unrelated, reply: "
            f"'Sorry, I can only talk about farming and agriculture-related topics.'\n\nUser: {prompt}"
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Connection issue: {e}"

# ---------------- SPEECH OUTPUT ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- MAIN CHAT AREA ----------------
st.markdown("### 🌱 Ask me anything about farming:")

user_input = st.text_input("Type your question here 👇")

if st.button("Get Answer"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            answer = get_ai_response(user_input)
        st.success("✅ Answer:")
        st.write(answer)
        if st.checkbox("🔊 Speak the answer"):
            speak(answer)
    else:
        st.warning("Please enter a question first.")

# ---------------- FOOTER ----------------
st.markdown("""
---
🌿 **KrishiVox | Team Naya Kal**  
_AI-Based Crop Recommendation and Farming Assistant_  
""")
