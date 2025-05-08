import random

def generate_quiz(course_data, num_questions=5):
    """Generate a quiz with random questions from course materials."""
    all_text = " ".join(course_data.values())
    sentences = [sentence for sentence in all_text.split('.') if sentence.strip()]
    
    # Pick random sentences as quiz questions
    questions = random.sample(sentences, min(len(sentences), num_questions))
    quiz = [{"question": question.strip(), "answer": "Write your answer here"} for question in questions]
    return quiz
