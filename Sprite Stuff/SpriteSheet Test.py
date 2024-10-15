import tkinter as tk
import pygame as pg
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')
root.title('Images')

image_original = Image.open('Squirrel.png')

class Animal:
    #Image splitter#
    #//NOTE: Will only read in squares!//#
    def FrameSplit(self, img, byteSize): #(Image File, Pixel Count)
        def appendList(l, ele):
            l.append(ele)
            return l

        framesY = [] 
        #Needed to get the spritesheet size
        x, y = img.size
        frameNumX = int(x/byteSize)
        frameNumY = int(y/byteSize)

        print(frameNumX, frameNumY)

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
                tempFramesX.append(tempImg)
                x += 1
            
            framesY = appendList(framesY, tempFramesX)
            y += 1
        
        return framesY
    def __init__(self, img, byteSize):
        self.img = img
        self.bitSiz = byteSize
        self.frame = self.FrameSplit(img, byteSize) 
    
    def FrameGet(self, y, x):
        image = self.frame[y][x]
        return image

squirrel = Animal(image_original, 32)

squirrel.FrameGet(0, 0).show()

#root.mainloop()