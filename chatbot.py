def chatbot():
    print("==== Welcome to Basic Chatbot ====")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user = input("You:").lower()
        if user=="hello":
            print("Bot: Hello! Welcome.")

        elif user=="hi":
            print("Bot: Hi! How are you.")

        elif user=="how are you?":
            print("Bot: I'm fine, thank you!")

        elif user=="what is your name?":
            print("Bot: My name is Basic chatbot")

        elif user=="who created you?":
            print("Bot: I was created using python.")

        elif user=="help":
            print("Bot: You can say hello, hi, how are you, what is your name, thank you or bye.")

        elif user=="thank you":
            print("Bot: You're welcome")

        elif user=="bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()