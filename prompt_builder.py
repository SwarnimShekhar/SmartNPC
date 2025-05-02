import random

def npc_asks_question(npc_name: str, conversation_history: list, game_state: dict) -> str:
    questions = [
        "Do you want to know more about this place?",
        "What do you think of the current situation?",
        "Are you ready for the challenges ahead?",
        "Would you like me to tell you about the forest's secrets?",
    ]

    if game_state.get('location') == "Abandoned Mine":
        questions.append("Do you have a plan for dealing with the creatures here?")

    return random.choice(questions)

def build_prompt_with_memory(npc_name, user_input, npc_data, history, game_state, max_turns=5):
    npc = npc_data.get(npc_name, {
        "name": npc_name,
        "role": "a mysterious figure",
        "personality": "neutral",
        "background": "unknown"
    })

    memory = f"Memory: {npc['background']}"
    recent_dialogue = history[-max_turns:] if history else []

    dialogue_context = '\n'.join([
        f"Player: {entry['user']}\n{entry['npc']}: {entry['reply']}"
        for entry in recent_dialogue
    ])

    npc_question = npc_asks_question(npc_name, history, game_state)

    return (
        f"You are {npc['name']}, a {npc['role']} in a fantasy world. "
        f"Your personality is: {npc['personality']}\n{memory}\n\n"
        f"{dialogue_context}\n"
        f"Player: {user_input}\n"
        f"{npc_name}:"
    )