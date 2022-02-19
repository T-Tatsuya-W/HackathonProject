from PIL import Image,ImageDraw,ImageFont
 
src1 = "sources/car.png"
img = Image.open(src1)
src2 = "sources/text.txt"
text = open(src2, "r")
Lines = text.readlines()    #each line is read into an array as a new objec


def writeWordsWithNewLines(font):
        fontType = font         #"arial" for Windows, "Arial" for Mac
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        #myFont = ImageFont.load_default()
        
        myFont = ImageFont.truetype(fontType, drawWords.size)

        textsize = myFont.getsize(drawWords.text)
        distanceRight = drawWords.x+textsize[0]

        
        print(drawWords.size)

        newText = drawWords.text.split()
        printString = ""
        #print(newText)
        sum = drawWords.x


        for a in range(len(newText)):
            printString += newText[a]
            printString += " "
            wordsize = myFont.getsize(printString)[0] + drawWords.x
            #print(wordsize)
            #sum = sum + myFont.getsize(a)[0]

            
            if a!=len(newText)-1:
                if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                    textPosition = (drawWords.x, drawWords.y) # (x, y) from top left
                    fontColour = (drawWords.R,drawWords.G,drawWords.B) #rgb colour values
                    I1.text(textPosition, printString, font=myFont, fill =fontColour)

                    drawWords.y=drawWords.y+drawWords.size
                    printString = ""

            else: 
                #if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                    textPosition = (drawWords.x, drawWords.y) # (x, y) from top left
                    fontColour = (drawWords.R,drawWords.G,drawWords.B) #rgb colour values
                    I1.text(textPosition, printString, font=myFont, fill =fontColour)

                    drawWords.y=drawWords.y+drawWords.size



def drawWords(text, x, y, R, G, B, size):   #doubled text writer to work with both windows and mac
    drawWords.text = text
    drawWords.x = x
    drawWords.y = y
    drawWords.R = R
    drawWords.G = G
    drawWords.B = B
    drawWords.size = size


    try:
        writeWordsWithNewLines("arial")

    except OSError:
        writeWordsWithNewLines("Arial")

    return drawWords.y
    


#draw 3 simple magentas lines from the text
nexty = drawWords(Lines[0], 20, 40, 255, 0, 255, 65)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 55)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 54)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 53)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 52)
nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 51)

#drawWords(Lines[2  ], 20, 280, 255, 0, 255, 65)


img.show()  #temporarily shows the created image

img.save(".gitignore/car2.png")    # Save the image
