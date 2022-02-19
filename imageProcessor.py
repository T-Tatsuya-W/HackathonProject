from PIL import Image,ImageDraw,ImageFont
 
src1 = "sources/car.png"
img = Image.open(src1)
src2 = "sources/text.txt"
text = open(src2, "r")
Lines = text.readlines()    #each line is read into an array as a new objec

print(img.width, img.height)

def drawWords(text, x, y, R, G, B, size):   #doubled text writer to work with both windows and mac
    try:
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        #myFont = ImageFont.load_default()
        fontType = "arial"              #"arial" for Windows, "Arial" for Mac
        myFont = ImageFont.truetype(fontType, size)

        textsize = myFont.getsize(text)
        distanceRight = x+textsize[0]
        if (distanceRight > img.width):
            newText = text.split()
            printString = ""
            #print(newText)
            sum = x

            for a in range(len(newText)):
                printString += newText[a]
                printString += " "
                wordsize = myFont.getsize(printString)[0] + x
                #print(wordsize)
                #sum = sum + myFont.getsize(a)[0]
                
                if a!=len(newText)-1:
                    if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                        textPosition = (x, y) # (x, y) from top left
                        fontColour = (R,G,B) #rgb colour values
                        I1.text(textPosition, printString, font=myFont, fill =fontColour)

                        y=y+size
                        printString = ""

                else: 
                    #if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                        textPosition = (x, y) # (x, y) from top left
                        fontColour = (R,G,B) #rgb colour values
                        I1.text(textPosition, printString, font=myFont, fill =fontColour)

                        y=y+size

        return y

            



    except OSError:
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size   
        #myFont = ImageFont.load_default()
        fontType = "Arial"              # "arial" for Windows, "Arial" for Mac
        myFont = ImageFont.truetype(fontType, size)

        
        textsize = myFont.getsize(text)
        distanceRight = x+textsize[0]
        if (distanceRight > img.width):
            newText = text.split()
            printString = ""
            #print(newText)
            sum = x

            for a in range(len(newText)):
                printString += newText[a]
                printString += " "
                wordsize = myFont.getsize(printString)[0] + x
                #print(wordsize)
                #sum = sum + myFont.getsize(a)[0]
                
                if a!=len(newText)-1:
                    if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                        textPosition = (x, y) # (x, y) from top left
                        fontColour = (R,G,B) #rgb colour values
                        I1.text(textPosition, printString, font=myFont, fill =fontColour)

                        y=y+size
                        printString = ""

                else: 
                    #if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                        textPosition = (x, y) # (x, y) from top left
                        fontColour = (R,G,B) #rgb colour values
                        I1.text(textPosition, printString, font=myFont, fill =fontColour)

                        y=y+size

        return y


#draw 3 simple magentas lines from the text
nexty = drawWords(Lines[0], 20, 40, 255, 0, 255, 65)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 55)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 54)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 53)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 52)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 51)

#drawWords(Lines[2], 20, 280, 255, 0, 255, 65)


img.show()  #temporarily shows the created image

img.save("car2.png")    # Save the image
