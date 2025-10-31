# -*- coding: utf-8 -*-
import streamlit as st
import google.generativeai as genai

# ---------------- CONFIG ----------------
genai.configure(api_key="AIzaSyDlZ-ws6X2uRdQ9dsJDIZpjdOoXk5z5Uas")
model = genai.GenerativeModel("gemini-2.0-flash")  # ✅ stable free model

# ---------------- STREAMLIT UI SETTINGS ----------------
st.set_page_config(page_title="KrishiSathi 🌿", page_icon="🌾", layout="centered")

# ---------------- STYLING ----------------
st.markdown(
    """
    <style>
        body { background-color: #f9fff9; color: #003300; }
        .stTextInput > div > div > input {
            border: 2px solid #3CB371; border-radius: 10px; padding: 8px;
        }
        .stButton > button {
            background-color: #3CB371; color: white; border-radius: 10px;
            font-weight: bold; padding: 8px 18px;
        }
        .stButton > button:hover { background-color: #2E8B57; }
        .mic-button {
            background-color: #3CB371; border: none; color: white;
            border-radius: 50%; padding: 10px; cursor: pointer;
        }
        .mic-button:hover { background-color: #2E8B57; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.title("🌾 KrishiSathi - Your AI Farming Assistant")
st.markdown("Ask me anything about **farming, crops, soil, irrigation, fertilizers, or weather.**")

# ---------------- CHAT INPUT ----------------
user_input = st.text_input("💬 Type your farming question below:")

# 🎤 Voice input section (via browser)
st.markdown("""
    <button id="mic" class="mic-button">🎙️</button>
    <p id="voiceText" style="color:green; font-weight:bold;"></p>

    <script>
        const micBtn = document.getElementById("mic");
        const voiceText = document.getElementById("voiceText");
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-IN';
        recognition.interimResults = false;

        micBtn.onclick = () => {
            voiceText.innerHTML = "🎤 Listening...";
            recognition.start();
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            voiceText.innerHTML = "🗣️ You said: " + transcript;
            const inputBox = window.parent.document.querySelector('input[type="text"]');
            inputBox.value = transcript;
            inputBox.dispatchEvent(new Event('input', { bubbles: true }));
        };
    </script>
""", unsafe_allow_html=True)

# ---------------- BUTTON ACTION ----------------
if st.button("Ask KrishiSathi"):
    if user_input.strip() == "":
        st.warning("Please enter a question or use the 🎙️ mic to speak.")
    else:
        with st.spinner("Thinking... 🌱"):
            try:
                response = model.generate_content(
                    f"You are KrishiSathi, an agricultural expert chatbot. "
                    f"You must only answer questions related to farming, crops, soil, irrigation, fertilizers, "
                    f"pesticides, weather, and agricultural technology. "
                    f"If the question is unrelated, say: "
                    f"'Sorry, I can only talk about farming and agriculture-related topics.'\n\nUser: {user_input}"
                )

                # ✅ Display answer
                st.success(response.text.strip())

                # 🔊 Speak the response in browser
                st.markdown(f"""
                    <script>
                        var utterance = new SpeechSynthesisUtterance("{response.text.strip().replace('"', "'")}");
                        utterance.lang = 'en-IN';
                        utterance.rate = 1;
                        utterance.pitch = 1;
                        speechSynthesis.speak(utterance);
                    </script>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ Error connecting to Gemini: {e}")

# ---------------- FOOTER ----------------
st.markdown("<hr><center>🌿 Developed by Team NayaKal | Powered by Gemini 🌿</center>", unsafe_allow_html=True)
