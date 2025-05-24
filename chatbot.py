import json
import os

# File to store chatbot memory
file_name = "chatbot_memory.json"

# Load existing memory or create new
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        memory = json.load(file)
else:
    memory = {}

print("Chatbot: Hello! I am your self-learning chatbot.")
print("Type 'bye' to exit.")
print("Type 'correct' to fix a wrong answer.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "bye":
        print("Chatbot: Goodbye! 👋")
        break

    elif user_input == "correct":
        # Ask which question to correct
        wrong_question = input("Which question do you want to correct? ").strip().lower()
        if wrong_question in memory:
            print("Current answer:", memory[wrong_question])
            new_answer = input("What should be the correct answer? ").strip()
            memory[wrong_question] = new_answer
            print("Chatbot: Got it! I have updated the response.")
            with open(file_name, "w") as file:
                json.dump(memory, file)
        else:
            print("Chatbot: I don’t know that question yet.")

    elif user_input in memory:
        print("Chatbot:", memory[user_input])
    else:
        print("Chatbot: I don't know how to respond to that.")
        new_response = input("Please teach me what I should reply: ").strip()
        memory[user_input] = new_response
        print("Chatbot: Thanks! I’ll remember that.")
        with open(file_name, "w") as file:
            json.dump(memory, file)