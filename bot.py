# bot.py
#region Imports
from asyncio.windows_events import NULL
import os
import discord
from dotenv import load_dotenv
import pandas as pd
import random as rnd
#endregion

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    #Checks if the message author is the bot to stop it from commanding itself
    if message.author == client.user:
        return
    #Fuck you artin
    if message.content.startswith('$artin'):
        await message.channel.send('Fuck off!')
    
    #Generates quote
    if message.content.startswith('$quote'): #checks a user has called the command
        #Declares new lis
        messagecontent = []
        messageauthor = []

        #Loops through the message history
        async for msg in message.channel.history(limit=100):
            if msg.author != client.user:
                if type(msg.content) == list:
                    break
                elif len(msg.content) < 1 or len(msg.content) > 25 or msg.content.startswith('$') == True:
                    continue
                else:
                    messagecontent.append(msg.content)
                    messageauthor.append(msg.author.name)

        x = rnd.randrange(len(messagecontent)-1)
        value = (messagecontent[x] + "\n" + messageauthor[x])
        print (value)
        await message.channel.send(value)
                       

#region OnReadyEvent
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
#endregion

client.run(TOKEN)
