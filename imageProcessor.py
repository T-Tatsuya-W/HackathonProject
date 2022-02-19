from PIL import Image,ImageDraw,ImageFont
 
# Open an Image in src
src1 = "sources/car.png"
img = Image.open(src1)
src2 = "sources/text.txt"
text = open(src2, "r")



 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Custom font style and font size
#myFont = ImageFont.load_default()
fontSize = 65
fontType = "arial"              #"arial" for Windows, "Arial" for Mac
myFont = ImageFont.truetype(fontType, fontSize)
 
textPosition = (20, 40) # (x, y) from top left
textContents = "Nice Car"
fontColour = (225,0,225) #rgb colour values
I1.text(textPosition, textContents, font=myFont, fill =fontColour)
 

img.show()  #temporarily shows the created image
 
img.save("car2.png")    # Save the image

