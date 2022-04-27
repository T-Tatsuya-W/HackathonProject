# bot.py
#region Imports
import os
import sys
import discord
from dotenv import load_dotenv
import random as rnd
import PIL
from PIL import Image, ImageDraw, ImageColor
from perlin_noise import PerlinNoise


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


        #HERE IS CONTENT TO CREATE IMAGE ---------------------------------------
        if rnd.random()>0.5:
            url = "https://source.unsplash.com/random"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            #img.show()
        else:
            xpix, ypix = 1000,1000
            img = Image.new("RGBA", (xpix, ypix), (20,20,20,255))
            noisex = PerlinNoise(octaves = 8)
            noisey = PerlinNoise(octaves = 8)
            noises = PerlinNoise(octaves = 4)
            noiseH = PerlinNoise(octaves = 4)
            hOrigin = rnd.random()*360
            for i in range(1000):
                line = (int(xpix/2 + noisex(i/500)*xpix), int( ypix/2 + noisey(i/500)*ypix))
                size =  15 + int(noises(i/1000)*30)
                hue =  int( hOrigin + (noiseH(i/1000)*360))
                if hue>= 360:
                    hue = hue - 360
                if hue < 0:
                    hue = hue +360
                rgb = ImageColor.getrgb("hsv("+str(hue)+",100%,100%)")
                transp = Image.new("RGBA", img.size, (0,0,0,0))
                draw = ImageDraw.Draw(transp, "RGBA")
                pos = ((line[0]-size, line[1]-size),(line[0]+size, line[1]+size))
                draw.ellipse(pos, fill = (rgb[0], rgb[1], rgb[2], 30))
                img.paste(Image.alpha_composite(img, transp))
        img.save("tempImage.png")

        #----------------------------------------------------------------------



        img = Image.open("tempImage.png")
        (width, height) = img.size
        total = 0
        for i in range(height):
            for j in range(width):
                colours = img.getpixel((j,i))
                total += colours[0]
                total += colours[1]
                total += colours[2]
        avg = total/(3*width*height)
        
        if avg < (255/2):
            rgb = 255
        else:
            rgb = 0




        image1 = IP.ImageHandler(rgb,rgb,rgb,50,"tempImage.png")
        #image1 = IP.ImageHandler(0,0,0,50,"sources/car.png")

        image1.setTextBoxDimensions()

        image1.fontPicker()

        image1.drawWords("\""+quote1+"\"", 0)

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


            #HERE IS CONTENT TO CREATE IMAGE ---------------------------------------

            url = "https://source.unsplash.com/random"
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            #img.show()
            img.save("tempImage.png")

            #----------------------------------------------------------------------

                
            img = Image.open("tempImage.png")
            (width, height) = img.size
            total = 0
            for i in range(height):
                for j in range(width):
                    colours = img.getpixel((j,i))
                    total += colours[0]
                    total += colours[1]
                    total += colours[2]
            avg = total/(3*width*height)
            
            if avg < (255/2):
                rgb = 255
            else:
                rgb = 0


            image1 = IP.ImageHandler(0,0,0,50,"tempImage.png")
            #image1 = IP.ImageHandler(0,0,0,50,"sources/car.png")

            image1.setTextBoxDimensions()

            image1.fontPicker()

            image1.drawWords("\""+reaction.message.content+"\"", 0)

            image1.drawWords(CS.generator(), 2)

            image1.saveImage()


            await reaction.message.channel.send(file=discord.File('output.png'))
            #--------------------------- Message after the image should be changed to something beter
            #await reaction.message.channel.send("Here is a comment to accompany the quote")

#region OnReadyEvent
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
#endregion

client.run(TOKEN)
