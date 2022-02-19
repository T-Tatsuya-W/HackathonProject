# bot.py
from asyncio.windows_events import NULL
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
        messagecontent = []
        messageauthor = []

        async for msg in message.channel.history(limit=100):
            if msg.author != client.user:
                #print("the current message is------"+msg.content)
                if type(msg.content) == list:
                    #print("has reached the end of the messages")
                    break
                else:
                    messagecontent.append(msg.content)
                    messageauthor.append(msg.author)
        print(messagecontent)                      

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
