import tkinter as tk
import pygame as pg
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')
root.title('Images')

image_original = Image.open('Desktop\Repository\Python Repository\Sophmore Project\Squirrel.png')

#Still a WIP, Turning this into a 2 x 2 array
class Animal:
    #Image splitter#
    #//NOTE: Will only read in squares!//#
    def FrameSplit(self, img, byteSize): #(Image File, Pixel Count)
        frame = []
        #Needed to get the spritesheet size
        x, y = img.size
        frameNumX = int(x/byteSize)
        frameRowY = int(y/byteSize)

        #Splits the image and adds them to an array
        i = 0
        while i < frameNumX:
            #Frame 1 Example: (x0, y0, x32, y32)
            j = byteSize * i
            tempImg = img.crop((0 + j, 0, byteSize + j, byteSize))        
            frame.append(tempImg)
            i += 1
        return frame

    def __init__(self, img, byteSize):
        self.img = img
        self.bitSiz = byteSize
        self.frame = self.FrameSplit(img, byteSize) 
    
    def FrameGet(self, x):
        image = self.frame[x]
        return image

squirrel = Animal(image_original, 32)
squirrel.FrameGet(3).show()

#root.mainloop()