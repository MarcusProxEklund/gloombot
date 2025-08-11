from interactions import Client, Intents, slash_command, SlashContext, listen,slash_option, OptionType
from dotenv import load_dotenv
import logging
import time
import sys
import os

from querying import data_querying

load_dotenv()

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# enable INFO level logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

bot = Client(intents=Intents.ALL)


@listen() 
async def on_ready():
    print(f"Gloombot is running...")
    # print(f"This bot is owned by {bot.owner}")


@slash_command(name="bot")
@slash_option(
    name="input_text",
    description="Enter your query:)",
    required=True,
    opt_type=OptionType.STRING,
)
async def get_response(ctx: SlashContext, input_text: str):
    time.perf_counter()  # Start the timer
    await ctx.defer()
    response = data_querying(input_text)
    response = f'**Input Query**: {input_text}\n\n{response}'
    await ctx.send(response)
    time.perf_counter()  # End the timer
    logging.info(f"Response sent in {time.perf_counter()} milliseconds.")


if __name__ == '__main__':
    bot.start(os.getenv("DISCORD_BOT_TOKEN"))