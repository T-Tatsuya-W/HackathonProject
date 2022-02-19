from PIL import Image,ImageDraw,ImageFont
 
# Open an Image in src
src1 = "sources/car.png"
img = Image.open(src1)
src2 = "sources/text.txt"
text = open(src2, "r")
Lines = text.readlines()    #each line is read into an array as a new objec

def drawWords(text, x, y, R, G, B, size):
    try:
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        #myFont = ImageFont.load_default()
        fontType = "arial"              #"arial" for Windows, "Arial" for Mac
        myFont = ImageFont.truetype(fontType, size)
        textPosition = (x, y) # (x, y) from top left
        fontColour = (R,G,B) #rgb colour values
        I1.text(textPosition, text, font=myFont, fill =fontColour)
    except OSError:
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        #myFont = ImageFont.load_default()
        fontType = "Arial"              #"arial" for Windows, "Arial" for Mac
        myFont = ImageFont.truetype(fontType, size)
        textPosition = (x, y) # (x, y) from top left
        fontColour = (R,G,B) #rgb colour values
        I1.text(textPosition, text, font=myFont, fill =fontColour)

        

drawWords(Lines[0], 20, 40, 255, 0, 255, 65)

drawWords(Lines[1], 20, 80, 255, 0, 255, 65)

drawWords(Lines[2], 20, 140, 255, 0, 255, 65)

img.show()  #temporarily shows the created image

img.save("car2.png")    # Save the image
