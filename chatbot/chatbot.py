
print("Welcome to CODE-A-NOVA Chatbot!")
name = ""

while True:
    message = input("You: ").strip().lower()

    if message in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif message == "help":
        print("Bot: You can say hello, tell me your name, or type bye.")

    elif message.startswith("my name is "):
        name = message[11:].strip().title()
        if name:
            print(f"Bot: Nice to meet you, {name}!")
        else:
            print("Bot: Please enter your name.")

    elif message == "name":
        if name:
            print(f"Bot: Your name is {name}.")
        else:
            print("Bot: You have not told me your name yet.")

    elif message in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Thank you for chatting.")
        break

    elif message == "":
        print("Bot: Please type something.")

    else:
        print("Bot: Sorry, I don't understand. Type 'help'.")
