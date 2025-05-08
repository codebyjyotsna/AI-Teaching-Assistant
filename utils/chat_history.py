import os
import json
from datetime import datetime

CHAT_HISTORY_DIR = './data/chat_history/'

def save_chat(user_id, question, response):
    """Save the chat history for a user."""
    if not os.path.exists(CHAT_HISTORY_DIR):
        os.makedirs(CHAT_HISTORY_DIR)
    
    history_file = os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json")
    
    # Create or load the user's chat history
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            chat_history = json.load(file)
    else:
        chat_history = []

    # Add the new chat entry
    chat_entry = {
        "timestamp": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "question": question,
        "response": response
    }
    chat_history.append(chat_entry)

    # Save the updated chat history
    with open(history_file, 'w') as file:
        json.dump(chat_history, file, indent=4)

def get_chat_history(user_id):
    """Retrieve chat history for a user."""
    history_file = os.path.join(CHAT_HISTORY_DIR, f"{user_id}.json")
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            return json.load(file)
    return []
