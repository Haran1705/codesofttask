def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    elif "name" in user_input:
        return "I am a simple chatbot. You can call me ChatGPT."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Example usage
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)