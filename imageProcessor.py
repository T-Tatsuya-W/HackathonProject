from PIL import Image,ImageDraw,ImageFont
import os, random, math

class ImageHandler():
    def __init__(self, R, G, B, size, src) -> None:
        self.R = R
        self.G = G
        self.B = B
        self.size = size
        self.text = ""
        self.myFont = ""
        self.fontType = ""

        self.textBoxes = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.image = Image.open(src)

    def getImage(self, src):
        self.image = Image.open(src)

    def drawWords(self, text, textBoxNo):
        self.text = text
        #ensures that the text is contained within the constraints of the image width

        I1 = ImageDraw.Draw(self.image)
        self.size = 50
        
        self.myFont = ImageFont.truetype("fonts/"+self.fontType, self.size)

        textsize = self.myFont.getsize(self.text)

        availableArea = (self.textBoxes[textBoxNo][2]-self.textBoxes[textBoxNo][0])*(self.textBoxes[textBoxNo][3]-self.textBoxes[textBoxNo][1])
        currentArea = textsize[0]*textsize[1]
        scaler = math.floor(availableArea)/math.ceil(currentArea)

        print(scaler)



        newFontSize = int(self.size * math.sqrt(scaler * 0.7))
        
        print("from "+str(self.size)+"to"+str(newFontSize))
        
        self.size = newFontSize
        print(self.size)
        self.myFont = ImageFont.truetype("fonts/"+self.fontType, int(self.size))
        print(self.myFont.getsize)

        distanceRight = self.textBoxes[textBoxNo][0]+textsize[0]

        newText = self.text.split()
        printString = ""
        sum = self.textBoxes[textBoxNo][0] #the total distance from the left

        for a in range(len(newText)):
            printString += newText[a]
            printString += " "
            wordsize = self.myFont.getsize(printString)[0] + self.textBoxes[textBoxNo][0]    #total distance to the right now that the word is added

            if a!=len(newText)-1:
                if wordsize + self.myFont.getsize(newText[a+1])[0] > self.textBoxes[textBoxNo][2]:
                    textPosition = (self.textBoxes[textBoxNo][0], self.textBoxes[textBoxNo][1]) # (x, y) from top left
                    fontColour = (self.R,self.G,self.B) #rgb colour values
                    I1.text(textPosition, printString, font=self.myFont, fill =fontColour)

                    self.textBoxes[textBoxNo][1] = self.textBoxes[textBoxNo][1] + self.size
                    printString = ""

            else: 
                textPosition = (self.textBoxes[textBoxNo][0], self.textBoxes[textBoxNo][1]) # (x, y) from top left
                fontColour = (self.R,self.G,self.B) #rgb colour values
                I1.text(textPosition, printString, font=self.myFont, fill =fontColour)
                self.textBoxes[textBoxNo][1] = self.textBoxes[textBoxNo][1] + self.size

    def saveImage(self):
        self.image.save("output.png")

    def main(self):
        self.image = Image.new('RGB', (1,1))
        self.image = self.getImage("sources/car.png")

    def setTextBoxDimensions(self):
        #convert to buffer percents rather than pixel values? to accomodate larger or smaller images

        self.textBoxes[0] = [50,50,self.image.width-50, int(self.image.height*(2/3)-50)]

        self.textBoxes[1] = [50, int(self.image.height*(2/3)) ,self.image.width-50, int(self.image.height*(5/6)-50)]

        self.textBoxes[2] = [50,int(self.image.height*(5/6)),self.image.width-50, self.image.height-50]

    def fontPicker(self):
        #fontType = "fonts/ArianaVioleta.ttf"
        self.fontType = random.choice(os.listdir("fonts/"))

        print(self.fontType)


