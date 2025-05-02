import streamlit as st
from model_engine import get_llm, generate_response
from prompt_builder import build_prompt_with_memory
from npc_data import npc_data
from game_state import game_state
from elevenlabs import ElevenLabs, play
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page settings
st.set_page_config(page_title="SmartNPC", page_icon="🧙‍♂️", layout="wide")

# Inject custom fantasy CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Wizard Banner and Title
st.markdown("""
    <div class="banner">
        <h1 class="glow-text">SmartNPC</h1>
        <p class="tagline">Whispers from the Wizard Tower</p>
    </div>
""", unsafe_allow_html=True)

# Load LLM once
@st.cache_resource
def load_llm():
    return get_llm()

llm = load_llm()

# Sidebar: NPC selection
st.sidebar.title("🎭 Choose Your NPC")
selected_npc = st.sidebar.selectbox("Select NPC", list(npc_data.keys()))

# ✅ Updated: Generate speech and play without saving
def generate_speech(npc_reply, selected_npc):
    try:
        voice_map = {
            "Elandor": "uju3wxzG5OhpWcoi3SMy",
            "Thrag": "2EiwWnXFnvU5JabPnv8n",
            "Lyra": "eVItLK1UvXctxuaRV2Oq"
        }

        voice_id = voice_map.get(selected_npc, "CYw3kZ02Hs0563khs1Fj")

        client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
        audio_stream = client.text_to_speech.convert(
            text=npc_reply,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )

        play(audio_stream)  # Play directly without saving
    except Exception as e:
        st.error(f"Exception during TTS: {e}")

# Main interaction section
if selected_npc:
    npc = npc_data[selected_npc]
    npc_avatar_url = npc.get("avatar_url", "https://i.imgur.com/t9HFQvX.png")

    st.markdown(f"""
        <div class="npc-header">
            <img src="{npc_avatar_url}" class="npc-avatar" />
            <h2 class="glow-text">Conversation with {selected_npc}</h2>
        </div>
    """, unsafe_allow_html=True)

    history = st.session_state.get("history", [])

    st.markdown("#### 🗨️ Speak to the NPC")
    with st.form(key="chat_form"):
        user_input = st.text_input("You:", key="input_box")
        submit = st.form_submit_button("Speak")

    if submit and user_input.strip():
        prompt = build_prompt_with_memory(
            npc_name=selected_npc,
            user_input=user_input,
            npc_data=npc_data,
            history=history,
            game_state=game_state,
            max_turns=5
        )

        with st.spinner("The winds of magic are stirring..."):
            npc_reply = generate_response(llm, prompt, stop_tokens=["Player:", f"{selected_npc}:"])
            generate_speech(npc_reply, selected_npc)

        history.append({
            "user": user_input,
            "reply": npc_reply,
            "npc": selected_npc
        })
        st.session_state.history = history

    if st.checkbox("🛠️ Show Debug Prompt"):
        if 'prompt' in locals():
            st.text_area("Debug Prompt", prompt, height=200)
    
    if history:
        st.markdown("---")
        st.markdown("### 📜 Scroll of Conversation")
        for message in reversed(history):
            st.markdown(f"""
                <div class="chat-bubble user-bubble">
                    <strong>You:</strong> {message['user']}
                </div>
                <div class="chat-bubble npc-bubble">
                    <strong>{message['npc']}:</strong> {message['reply']}
                </div>
            """, unsafe_allow_html=True)

    st.markdown("### 🧹 Reset Spell")
    if st.button("Clear Conversation"):
        st.session_state.history = []
        st.rerun()

# Footer
st.markdown("""<footer>🔮 Crafted in the Tower | 🌟 SmartNPC 2025</footer>""", unsafe_allow_html=True)