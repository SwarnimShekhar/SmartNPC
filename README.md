# 🧙‍♂️ SmartNPC: AI-Powered Conversational NPCs for Games

**SmartNPC** brings your game characters to life with immersive voice-based conversations, unique personalities, and seamless real-time interaction — powered by Groq and voiced through ElevenLabs.

<div align="center">
  <img src="https://i.imgur.com/d5RH7lU.png" alt="Elandor" height="180"/>
  <img src="https://i.imgur.com/pe0Xnue.jpeg" alt="Thrag" height="180"/>
  <img src="https://i.pinimg.com/564x/da/1b/b2/da1bb2353f6e484dd74287a8e312ae46.jpg" alt="Lyra" height="180"/>
</div>

---

## 🚀 Live Demo Preview

Watch 5-minute cinematic walkthrough where a player communicate with Elandor, Thrag, and Lyra in a fully dynamic setting (Use earphones or speakers for better audio experience).

https://github.com/user-attachments/assets/38d2177b-6a72-4004-a6ef-9f56e5c1522c



---

## 🎮 Features

✅ **Conversational AI NPCs**  
Each character has a defined role, backstory, and tone — responses feel natural and aligned with their persona.  

✅ **Real-Time Voice Output**  
Using the official ElevenLabs SDK, NPC replies are instantly spoken aloud with expressive voice synthesis.  

✅ **LLM Backend**  
Powered by `llama3-8b-8192` running via `Groq`, with fast, cloud based inference.  

✅ **Dynamic NPC Switching**  
Change between characters (Elandor, Thrag, Lyra) in one click — background, avatar, and behavior all update live.  

✅ **Cinematic Streamlit UI**  
Wizard Tower theme with animated avatars, fantasy fonts, and mood-matching visuals.  

✅ **Context-Aware Game State**  
Characters respond based on `location`, `time_of_day`, and recent `player_action`.

---

## 🧠 NPC Profiles

| Name    | Role                | Personality                   | Background                                                   |
|---------|---------------------|-------------------------------|--------------------------------------------------------------|
| Elandor | Wise Elven Mage     | Calm, cryptic, intelligent     | Guardian of ancient magic in the forest of Eldwyn           |
| Thrag   | Gruff Dwarven Smith | Blunt, practical, loyal        | Veteran of the Iron Wars, now crafting weapons in Emberdeep |
| Lyra    | Mysterious Rogue    | Cunning, witty, unpredictable  | Underworld operative from the shadows of Veloria            |

---

## 🛠️ Tech Stack

| Layer         | Tech                                       |
|---------------|--------------------------------------------|
| Frontend      | Streamlit + Custom CSS Theme (Wizard Tower)|
| Backend       | Python, groq, ElevenLabs SDK               |
| Model         | llama3-8b-8192                             |
| Voice         | ElevenLabs API (custom voices supported)   |
| Inference     | CPU/GPU supported                          |
---

## 📁 Project Structure
<pre> ``` 
  SmartNPC/ 
  │
  ├── app.py # Main Streamlit app with UI and logic
  ├── model_engine.py # Loads and runs the TinyLLaMA model
  ├── game_state.py # Manages player and game state
  ├── npc_data.py # Stores NPC details and voice mappings
  ├── prompt_builder.py # Builds prompts dynamically for each interaction
  ├── styles.css # Custom cinematic CSS for 'Wizard Tower' theme
  │ └── README.md # Project overview and documentation
  ``` </pre>

---

## 🧪 Quickstart (Local Setup)

### 1. Clone & Install
```bash
git clone https://github.com/SwarnimShekhar/SmartNPC.git
cd SmartNPC
```
### 2. Add Your ElevenLabs Key
Create a .env file:
```bash
ELEVEN_API_KEY=your_api_key_here
```
### 3. Launch App
```bash
streamlit run app.py
```
## 🧩 Requirements
- Python 3.10+

- ElevenLabs account + API key

- Groq model: llama3-8b-8192

## ✨ What's Next
- 🎤 Microphone input for 2-way voice chat

- 🧭 Procedural story engine + branching quest logic

- 🕹️ NPC memory persistence

- 🌐 Optional RAG support using game lore

## 🤝 Credits
- Voice: ElevenLabs

- Model: Groq

## 📣 Connect with Me
Swarnim Shekhar
👨‍💻 Data Science | 🧠 AI/ML
🔗 [LinkedIn](https://www.linkedin.com/in/swarnim-shekhar/)
🌟 If you liked this project, consider giving it a ⭐!
