# Rule-Based AI Chatbot
# DecodeLabs Project 1

print("🤖 AI Chatbot Started!")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    # Greetings
    elif user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine and ready to assist you!")

    elif user_input == "your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "bye":
        print("Bot: Bye! See you again.")

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")