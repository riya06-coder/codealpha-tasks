"""
basic chatbot
input from user like: "hello", "how are you","bye"
predefined replies like : "hii!" , "i'm fine,thanks!" ,"goodbye!"

key concepts used : if-elif, functions , loops, input/output.


 """


# A simple rule-based chatbot

def simple_chatbot():
    """
    This function runs a simple chatbot based on predefined rules.
    """
    print("Chatbot: Hello! I am a simple chatbot. You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I didn't understand that. Please try one of the commands.")

# Call the function to start the chatbot
simple_chatbot()

# fix: pause the window from closing
input("\nPress Enter to exit...")
