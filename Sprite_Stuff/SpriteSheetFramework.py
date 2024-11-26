import os as os
from PIL import Image

#Counts the number of files in Sprites, needed to make the array
def count_files(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
cd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
dp = cd + "\SpriteFolder"
file_count = count_files(dp)

#List of all animals
critterList = []

i = 0
while i < file_count:
    #Files are named in a s# format
    try:
        crit = Image.open(cd + "/SpriteFolder/s" + str(i) + ".png")
        critterList.append(crit)
        i = i + 1
    except:
        i = i + 1

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
            if colorI == "[(16384, (0, 0, 0, 0))]":
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
        byteSize = 128
        self.frame = self.FrameSplit(img, byteSize) 
    
    def FrameGet(self, y, x):
        image = self.frame[y][x]
        return image

#squirrel = Animal(0)
#squirrel.FrameGet(1, 4).show()
#print(squirrel.FrameGet(0, 0).getcolors())
