# bot.py
import os

import discord
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$artin'):
        await message.channel.send('Fuck off!')
    if message.content.startswith('$quote'):
        data = []
        async for msg in message.channel.history(limit=100):
            if msg.author != client.user:
                data = data.append(msg.content)
            if len(data) == 100:
                break
        print(data)                      

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
