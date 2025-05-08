import os

def load_course_materials(directory):
    """Load and preprocess course materials from text files."""
    course_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                course_data[filename] = file.read()
    return course_data
