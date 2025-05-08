import openai

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

def ask_question(question, course_data):
    """Ask a question to OpenAI's GPT model, using course materials."""
    context = "\n\n".join(course_data.values())
    prompt = f"Course materials:\n{context}\n\nQuestion: {question}\nAnswer:"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
