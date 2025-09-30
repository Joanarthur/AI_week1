def format_response(response):
    return f"**{response}**"

def validate_input(user_input):
    return isinstance(user_input, str) and len(user_input) > 0

def extract_keywords(user_input):
    return [word.lower() for word in user_input.split() if word.isalnum()]