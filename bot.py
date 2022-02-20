# bot.py
#region Imports
import os
import sys
import discord
from dotenv import load_dotenv
import random as rnd

#image processor for image handling
from PIL import Image,ImageDraw,ImageFont
import imageProcessor as IP
# sys.path.append('./Constructor')
import constructror_preqoute as CS
CS.generator()
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
                elif len(msg.content) < 1 or len(msg.content) > 100 or msg.content.startswith('$') == True or msg.content.startswith('http'):
                    continue
                else:
                    messagecontent.append(msg.content)
                    messageauthor.append(msg.author.name)

        x = rnd.randrange(len(messagecontent)-1)
        #value = (messagecontent[x] + "\n" + messageauthor[x])
        #print (value)

        quote1 = messagecontent[x]
        print("Generating quote from "+messageauthor[x])

        print(messagecontent[x])


        quote2 = "Author name"
        quote3 = CS.generator()

        #---------------------added image code
        #------------------------R,G,B,fontSize,img source

        import requests
        from io import BytesIO

        url = "https://source.unsplash.com/random"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        #img.show()
        img.save("tempImage.png")



        image1 = IP.ImageHandler(0,0,0,50,"tempImage.png")
        #image1 = IP.ImageHandler(0,0,0,50,"sources/car.png")

        image1.setTextBoxDimensions()

        image1.fontPicker()

        image1.drawWords(quote1, 0)

        #image1.drawWords(quote2, 1)

        image1.drawWords(quote3, 2)

        image1.saveImage()

        await message.channel.send(file=discord.File('output.png'))
        #--------------------------- Message after the image should be changed to something beter
        await message.channel.send("Here is a comment to accompany the quote")


@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        emoji = reaction.emoji
        if str(emoji) == "💬":
            print("aaa")
            import requests
            from io import BytesIO

            url = "https://source.unsplash.com/random"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            #img.show()
            img.save("tempImage.png")

            image1 = IP.ImageHandler(0,0,0,50,"tempImage.png")
            #image1 = IP.ImageHandler(0,0,0,50,"sources/car.png")

            image1.setTextBoxDimensions()

            image1.fontPicker()

            image1.drawWords(reaction.message.content, 0)

            image1.drawWords(reaction.message.author.name, 1)

            image1.saveImage()


            await reaction.message.channel.send(file=discord.File('output.png'))
            #--------------------------- Message after the image should be changed to something beter
            await reaction.message.channel.send("Here is a comment to accompany the quote")

#region OnReadyEvent
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
#endregion

client.run(TOKEN)
