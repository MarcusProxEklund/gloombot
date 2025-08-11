# Gloombot

## Gloomhaven: Jaws of the Lion Chatbot

![](thesis/appendix/gloombotdiscord.gif)

Gloombot is an intelligent Discord chatbot assistant for **Gloomhaven: Jaws of the Lion**. It leverages Retrieval-Augmented Generation (RAG) to provide instant, accurate rule clarifications and glossary lookups during gameplay, enhancing the tabletop experience for all players.

---

## Features

- **Natural Language Rule Queries:**
	- Ask questions about rules, scenarios, or glossary terms in plain English.
- **Retrieval-Augmented Generation (RAG):**
	- Combines semantic search with a large language model for grounded, context-aware answers.
- **Optimized for Gloomhaven: Jaws of the Lion:**
	- Uses a vector database built from the official glossary and rules.
- **Discord Integration:**
	- Interact with the bot directly in your Discord server via slash commands.
- **Real-Time Play Support:**
	- Fast responses to keep your game flowing.

---

## How It Works

1. **User submits a question** via a Discord slash command.
2. **Gloombot retrieves relevant context** from the Gloomhaven glossary using vector search (Cosine Similarity).
3. **A language model generates a response** grounded in the retrieved context.
4. **The answer is sent back** to the Discord channel, including the original query and the sourced explanation.

---

## Getting Started

### Prerequisites
- Python 3.10+
- Discord bot token ([How to create a bot](https://discord.com/developers/applications))
- OpenAI API key ([Get an API key](https://platform.openai.com/account/api-keys))
- [uv](https://github.com/astral-sh/uv) or `pip`

### Installation


1. **Clone the repository:**
    ```bash
    git clone https://github.com/MarcusProxEklund/gloombot.git
    cd gloombot
    ```
2. **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    # or
    pip install -r requirements.txt
    ```
3. **Set up your environment:**
    - Create a `.env` file with your Discord bot token and OpenAI API key:
      ```env
      DISCORD_BOT_TOKEN=your_token_here
      OPENAI_API_KEY=your_openai_key_here
      ```
4. **Run the bot:**
    ```bash
    uv python gloombot.py
    # or
    python gloombot.py
    ```
5. **Invite the bot to your Discord server:**
    - Use the OAuth2 URL generated in the Discord Developer Portal to invite Gloombot to your server.

---

## Usage

- In your Discord server, use the `/bot` slash command and enter your rules question.
- Example:
	> `/bot input_text: How do I get items?`

---

## Project Structure

```
embedding.py         # Embedding and vector database logic
querying.py          # Query handling and RAG pipeline
gloombot.py          # Main bot logic and command handling
thesis/              # Thesis and documentation
chroma/              # Vector database files
...
```

---

## Evaluation

- **RAG Triad Framework:**
	- Context relevance
	- Groundedness
	- Answer relevance
- **Playtesting:**
	- Validated with real Gloomhaven sessions

---

## References
- [Gloomhaven: Jaws of the Lion](https://boardgamegeek.com/boardgame/291457/gloomhaven-jaws-lion)
- [RAG Triad](https://truera.com/blog/the-rag-triad-framework/)
- [Discord Developer Portal](https://discord.com/developers/docs/intro)

---

## Acknowledgements

- Inspired by the Gloomhaven community
- Built with Python, [Discord.py](https://discordpy.readthedocs.io/), [ChromaDB](https://www.trychroma.com/), [ChatGPT](https://platform.openai.com/docs/models/gpt-4), and Retrieval-Augmented Generation (RAG) techniques.
