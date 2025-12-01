import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Load external CSS
def load_css():
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Setup Page
st.set_page_config(page_title="GymGenie", page_icon="💪", layout="centered")

# Load CSS
load_css()

# Header
st.markdown("""
    <div class="header-container">
        <div class="icon-container">
            <span class="icon">💪</span>
        </div>
        <h1 class="main-title">GymGenie - Virtual Trainer</h1>
        <p class="subtitle">Your personal fitness companion powered by AI-driven guidance,<br>boosting productivity and accessibility</p>
    </div>
""", unsafe_allow_html=True)

# Define the System Prompt
SYSTEM_INSTRUCTION = """
You are a virtual gym assistant.

PROTOCOL:
1. Ask the user for their weight, age, desired weight, and height immediately.
2. Only answer questions related to health, fitness, diet, and gym.
3. If the user asks about anything outside this scope (e.g. politics, movies), reply exactly: "I have no idea, that's not my job."
4. Provide recommendations for diet and health based on their goals.
5. talk only with the native egyption language 
"""

# Initialize Client & Chat
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": SYSTEM_INSTRUCTION}
    )
    # Optional: Send a hidden prompt to prime the bot to ask the first question
    response = st.session_state.chat.send_message("Start the intake process.")
    st.session_state.messages = [{"role": "assistant", "content": response.text}]


# Display Chat Interface
for msg in st.session_state.messages:
    role_class = "user-message" if msg["role"] == "user" else "assistant-message"
    st.markdown(f'<div class="message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)


# Chat input
if prompt := st.chat_input("Ask me about workouts, nutrition, or fitness goals..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Bot response
    with st.spinner("Thinking..."):
        response = st.session_state.chat.send_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    st.rerun()
