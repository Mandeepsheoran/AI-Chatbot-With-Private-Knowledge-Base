from query_engine import get_query_engine


def main():
    print("\n🧠 Welcome to Your Private RAG Chatbot! Type 'exit' to quit.\n")
    engine = get_query_engine()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = engine.query(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()