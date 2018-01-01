# -*- coding:utf-8 –*-
import numpy as np
import fileinput
from PIL import Image, ImageDraw, ImageFont

np.random.seed(526490)

color = 256*256*256*np.random.rand(256) #generate random color list

binNumMap = []

filepath = fileinput.input("C:/Users/Jovan/Desktop/new_map.txt")

width = 0
height = 0

for line in filepath:
    height += 1
    list = line.strip().split("|")
    del list[0]     #delete space in the list header
    del list[-1]    #delete space in the list tail
    binNumMap.append(list)
    width = len(list)

im = Image.new('RGB', (100*width, 100*height), 'white')

drawObject = ImageDraw.Draw(im)

Font1 = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",36)

for j in range(height):
    for i in range(width):
        drawObject.rectangle((100*i, 100*j, 100*i+100, 100*j+100), fill = int(color[int(binNumMap[j][i])]), outline='white')
        drawObject.text([100*i + 50-len(str(binNumMap[j][i]))*36/4, 100*j + 50-36/2], str(binNumMap[j][i]), font=Font1)

im.show()
im.save("test.png")