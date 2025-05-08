def recommend_resources(chat_history, course_data):
    """Recommend resources based on missed topics in chat history."""
    missed_topics = []
    for entry in chat_history:
        if "I don't understand" in entry["response"] or "Please explain" in entry["response"]:
            missed_topics.append(entry["question"])
    
    recommendations = []
    for topic in missed_topics:
        for file, content in course_data.items():
            if topic.lower() in content.lower():
                recommendations.append({"file": file, "content": content[:200] + "..."})
                break
    return recommendations
