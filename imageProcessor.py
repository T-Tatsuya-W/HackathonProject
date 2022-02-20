from PIL import Image,ImageDraw,ImageFont

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
        sum = self.x

        for a in range(len(newText)):
            printString += newText[a]
            printString += " "
            wordsize = myFont.getsize(printString)[0] + self.x

            if a!=len(newText)-1:
                if wordsize + myFont.getsize(newText[a+1])[0] > self.image.width:
                    textPosition = (self.x, self.y) # (x, y) from top left
                    fontColour = (self.R,self.G,self.B) #rgb colour values
                    I1.text(textPosition, printString, font=myFont, fill =fontColour)

                    self.y=self.y+self.size
                    printString = ""

            else: 
                textPosition = (self.x, self.y) # (x, y) from top left
                fontColour = (self.R,self.G,self.B) #rgb colour values
                I1.text(textPosition, printString, font=myFont, fill =fontColour)
                self.y=self.y+self.size

    def saveImage(self):
        self.image.save("car2.png")

    def main(self):
        self.image = Image.new('RGB', (1,1))
        self.image = self.getImage("sources/car.png")


    def drawWords(self): 
        #first tries "arial" for Windows, if not, "Arial" for mac
        try:
            self.writeWordsWithNewLines("fonts/ArianaVioleta.ttf")

        except OSError:
            self.writeWordsWithNewLines("Arial")

        #returns bottom y value for next draw functions to use as the top value
        return self.y
