import ollama
import sys

MODEL = "gemma4:e2b"

def chat():
    print(f"Modelo {MODEL} listo. Escribe 'exit' para salir.\n")

    messages = []

    while True:
        try:
            user_input = input("Tú: ")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break

        if user_input.strip().lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        # llamada optimizada tipo ollama run
        stream = ollama.chat(
            model=MODEL,
            messages=messages,
            stream=True,
            keep_alive=300,  # mantiene modelo en RAM
            options={
                "temperature": 0.7,
                "num_ctx": 2048,
            }
        )

        print("Gemma: ", end="", flush=True)

        full_reply = ""

        # streaming en tiempo real
        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                content = chunk["message"]["content"]
                sys.stdout.write(content)
                sys.stdout.flush()
                full_reply += content

        print()  # salto de línea final

        messages.append({"role": "assistant", "content": full_reply})


if __name__ == "__main__":
    chat()
