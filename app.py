from flask import Flask, request, jsonify, render_template
from utils.openai_api import ask_question
from utils.preprocess import load_course_materials
from utils.chat_history import save_chat, get_chat_history
from utils.quiz import generate_quiz
from utils.translate import translate_text
from utils.recommendations import recommend_resources
from utils.admin_dashboard import generate_dashboard

app = Flask(__name__)

# Load course materials
course_data = load_course_materials('./data/course_materials/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('question', '')
    user_id = request.json.get('user_id', 'anonymous')
    if not user_query:
        return jsonify({"error": "No question provided"}), 400
    
    # Generate response
    response = ask_question(user_query, course_data)
    
    # Save chat
    save_chat(user_id, user_query, response)
    
    return jsonify({"response": response})

@app.route('/history', methods=['GET'])
def history():
    user_id = request.args.get('user_id', 'anonymous')
    history = get_chat_history(user_id)
    return jsonify({"history": history})

@app.route('/quiz', methods=['GET'])
def quiz():
    quiz = generate_quiz(course_data)
    return jsonify({"quiz": quiz})

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json.get('text', '')
    language = request.json.get('language', 'es')
    translated = translate_text(text, language)
    return jsonify({"translated_text": translated})

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', 'anonymous')
    chat_history = get_chat_history(user_id)
    recommendations = recommend_resources(chat_history, course_data)
    return jsonify({"recommendations": recommendations})

@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
    # For simplicity, assume all chat history files belong to users
    import os
    import json
    chat_histories = {}
    history_dir = './data/chat_history/'
    if os.path.exists(history_dir):
        for filename in os.listdir(history_dir):
            if filename.endswith('.json'):
                with open(os.path.join(history_dir, filename), 'r') as file:
                    chat_histories[filename.replace('.json', '')] = json.load(file)
    
    dashboard_data = generate_dashboard(chat_histories)
    return jsonify({"dashboard": dashboard_data})

if __name__ == '__main__':
    app.run(debug=True)
