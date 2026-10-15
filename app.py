def get_response(message):
    text = message.lower().strip()

    if not text:
        return "Please type something!"

    if "hello" in text or "hi" in text:
        return "Hello! Welcome to BasicBot!"

    elif "your name" in text:
        return "My name is BasicBot."

    elif "how are you" in text:
        return "I am fine! How are you?"

    elif "python" in text:
        return "Python is a beginner-friendly programming language."

    elif "ai" in text:
        return "AI means Artificial Intelligence."

    elif "computer" in text:
        return "A computer processes data and gives output."

    elif "thank" in text:
        return "You're welcome!"

    elif "bye" in text:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't know that answer yet."


print("===== BASIC AI CHATBOT =====")
print("Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = get_response(user_message)
    print("BasicBot:", response)

    if user_message.lower().strip() == "bye":
        break