"""
TASK 4: Basic Chatbot
A simple rule-based chatbot that responds to predefined inputs.
"""

import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! How can I help you?"],
    "hi": ["Hi!", "Hello there!"],
    "how are you": ["I'm fine, thanks!", "Doing great, how about you?"],
    "what is your name": ["I'm a simple rule-based chatbot.", "You can call me ChatBot."],
    "help": ["I can chat about basic things. Try saying hello, asking how I am, or say bye to exit."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
}

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I didn't get that. Try saying 'help' to see what I can do.",
    "Hmm, I don't know how to respond to that.",
]


def get_response(user_input):
    """Match user input against known phrases and return an appropriate response."""
    text = user_input.lower().strip()

    for trigger, responses in RESPONSES.items():
        if trigger in text:
            return random.choice(responses)

    return random.choice(DEFAULT_RESPONSES)


def chat():
    print("Chatbot: Hello! Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    chat()
