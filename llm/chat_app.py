import ollama

def chat():
    print("chat listo. Escribe 'exit' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'exit': break
        
        response = ollama.chat(model='gemma:2b', messages=[
            {'role': 'user', 'content': user_input},
        ])
        print(f"Gemma: {response['message']['content']}")

if __name__ == "__main__":
    chat()
