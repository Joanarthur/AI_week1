from chatbot.bot import CryptoBuddy

def main():
    # Initialize the chatbot
    chatbot = CryptoBuddy()
    
    print("Welcome to the Cryptocurrency Advisor Chatbot!")
    print("Ask me anything about cryptocurrency investment advice.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        response = chatbot.respond_to_query(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()