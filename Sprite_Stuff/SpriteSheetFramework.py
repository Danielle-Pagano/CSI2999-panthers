import os as os
from PIL import Image

cd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#print(cd)

critterList = []

#This will change to check every file within file "Sprites" and add to critterList array
Squirrelsprite = "STS.png"
crit1 = Image.open(cd + "/" + Squirrelsprite)
critterList.append(crit1)

#Animal Class Object
class Animal:
    #Image splitter#
    #//NOTE: Will only read in squares!//#
    def FrameSplit(self, img, byteSize): #(Image File, Pixel Count)

        framesY = [] 
        
        def appendList(l, element):
            l.append(element)
            return l
        
        # Checks if the Image has any colors, returns false if no color is found
        def imgCheck(i):
            j = True
            colorI = str(i.getcolors())
            if colorI == "[(1024, (0, 0, 0, 0))]":
                j = False
            return j

        #Needed to get the spritesheet size
        x, y = img.size
        frameNumX = int(x/byteSize)
        frameNumY = int(y/byteSize)

        #Splits the image and adds them to an array
        y = 0
        while y < frameNumY:
            tempFramesX = []
            x = 0
            while x < frameNumX:
                #Frame 1 Example: (x0, y0, x32, y32)
                j = byteSize * x
                k = byteSize * y
                tempImg = img.crop((0 + j, 0 + k, byteSize + j, byteSize + k)) 
                if imgCheck(tempImg) == True:
                    tempFramesX.append(tempImg)
                x += 1
            framesY = appendList(framesY, tempFramesX)
            y += 1

        return framesY

    def __init__(self, choice):
        img = critterList[choice]
        byteSize = 32
        self.frame = self.FrameSplit(img, byteSize) 
    
    def FrameGet(self, y, x):
        image = self.frame[y][x]
        return image
