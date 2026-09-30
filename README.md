# PersonalChatBot

A personal chatbot that answers questions about me. It loads my background
from `about_me.md` and uses an LLM through OpenRouter to respond in a
friendly, professional tone, without making things up.

## Setup

1. Clone the repo and install dependencies: `uv sync`
2. Create a `.env` file with your key: `OPENROUTER_API_KEY=your_key_here`
3. Edit `src/personalchatbot/about_me.md` with your own details
4. Run: `uv run python -c "from personalchatbot import main; main()"`
