from collections import Counter

def generate_dashboard(chat_histories):
    """Generate admin dashboard details."""
    all_questions = [entry["question"] for history in chat_histories.values() for entry in history]
    common_questions = Counter(all_questions).most_common(5)
    
    usage_stats = {
        "total_users": len(chat_histories),
        "total_questions": len(all_questions),
        "most_common_questions": common_questions
    }
    return usage_stats
