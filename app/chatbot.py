def generate_response(message: str) -> str:
    if "hello" in message.lower():
        return "Hi there! How can I help you today?"
    elif "fees" in message.lower():
        return "The fee payment deadline is June 10th."
    else:
        return "Sorry, I didn't get that. Can you rephrase?"

//