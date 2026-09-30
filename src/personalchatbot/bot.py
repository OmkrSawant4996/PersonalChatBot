import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

MODEL = "openai/gpt-4o-mini"  # any model ID from openrouter.ai/models

ABOUT_ME = (Path(__file__).parent / "about_me.md").read_text(encoding="utf-8")

SYSTEM_PROMPT = f"""You are a chatbot that answers questions about Your Name.
Be friendly and professional. Answer ONLY using the information below.
If the answer isn't there, say you don't know and suggest contacting them
directly. Never make things up.

<about_me>
{ABOUT_ME}
</about_me>"""


def chat() -> None:
    history = []
    print("Ask me anything (type 'exit' to quit)\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        history.append({"role": "user", "content": question})

        reply = ""
        print("Bot: ", end="")
        stream = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *history],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                print(text, end="", flush=True)
                reply += text
        print("\n")
        history.append({"role": "assistant", "content": reply})