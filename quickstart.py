import anthropic
import os




MODEL = "claude-sonnet-5-5"
MAX_TOKENS = 512


ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
    api_key = os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://api.anthropic.com")

messages = []



print("Claude Chatbot")
print("Type /exit to quit.")

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "/exit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)

    try:
        with client.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)

            assistant_text = stream.get_final_text()

    except anthropic.APIError as error:
        messages.pop()
        print(f"\nRequest failed: {error}")
        continue

    messages.append({"role": "assistant", "content": assistant_text})
    print()