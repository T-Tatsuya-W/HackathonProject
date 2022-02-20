from PIL import Image,ImageDraw,ImageFont
"""
src1 = "sources/car.png"
img = Image.open(src1)
src2 = "sources/text.txt"
text = open(src2, "r")
Lines = text.readlines()   
"""
#----------------------------------------------------------------------------------------------


class ImageHandler():
    def __init__(self, text, x, y, R, G, B, size, src) -> None:
        self.x = x
        self.y = y
        self.R = R
        self.G = G
        self.B = B
        self.size = size
        self.text = text

        self.image = Image.open(src)

    def getImage(self, src):
        self.image = Image.open(src)


    def writeWordsWithNewLines(self, font):
        #global img
        #Code for drawing a string, taking the variables passed into (def drawWords)
        #ensures that the text is contained within the constraints of the image width

        print("successfully called writeWordsWithNewLines")
        fontType = font
        
        I1 = ImageDraw.Draw(self.image)

        
        myFont = ImageFont.truetype(fontType, self.size)

        textsize = myFont.getsize(self.text)
        distanceRight = self.x+textsize[0]

        
        print(self.size)

        newText = self.text.split()
        printString = ""
        #print(newText)
        sum = self.x


        for a in range(len(newText)):
            printString += newText[a]
            printString += " "
            wordsize = myFont.getsize(printString)[0] + self.x
            #print(wordsize)
            #sum = sum + myFont.getsize(a)[0]

            
            if a!=len(newText)-1:
                if wordsize + myFont.getsize(newText[a+1])[0] > self.image.width:
                    textPosition = (self.x, self.y) # (x, y) from top left
                    fontColour = (self.R,self.G,self.B) #rgb colour values
                    I1.text(textPosition, printString, font=myFont, fill =fontColour)

                    self.y=self.y+self.size
                    printString = ""

            else: 
                #if wordsize + myFont.getsize(newText[a+1])[0] > img.width:
                    textPosition = (self.x, self.y) # (x, y) from top left
                    fontColour = (self.R,self.G,self.B) #rgb colour values
                    I1.text(textPosition, printString, font=myFont, fill =fontColour)

                    self.y=self.y+self.size

    def saveImage(self):
        self.image.save("car2.png")



    def main(self):
        self.image = Image.new('RGB', (1,1))
        self.image = self.getImage("sources/car.png")
        #self.drawWords('hi', 20, 10, 0, 0, 0, 50, img)



    def drawWords(self): 
        #first tries "arial" for Windows, if not, "Arial" for mac
        try:
            self.writeWordsWithNewLines("arial")

        except OSError:
            self.writeWordsWithNewLines("Arial")

        #returns bottom y value for next draw functions to use as the top value
        return self.y


    

# ##

# def main():
#     img = Image.new('RGB', (1,1))
#     img = getImage("sources/car.png")
#     drawWords('hi', 20, 10, 0, 0, 0, 50, img)
    
# """
# #draws basic lines to test the auto newline, even this should be automated
# nexty = drawWords(Lines[0], 20, 40, 255, 0, 255, 65)
# nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 55)
# nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 54)
# nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 53)
# nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 52)
# nexty = drawWords(Lines[1], 20, nexty+30, 255, 0, 255, 51)


# #automatically shows the current state of img
# img.show()  #temporarily shows the created image


# #saves img to the directory indicated
# img.save(".gitignore/car2.png")    # Save the image"""
