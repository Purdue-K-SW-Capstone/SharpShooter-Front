from PIL import Image
import numpy as np
im = Image.open('C:/python/apple_sweet/nukki_apples/2-1.png')
pix = np.array(im)
c = np.arange(1,im.size[0],10)
d = np.arange(1,im.size[1],10)
red_sum = 0
green_sum = 0
blue_sum = 0
most_yellow = 0
count = 0
for i in c:
  for j in d:
    if pix[j][i][0] > 1:
      red_sum = red_sum + pix[j][i][0]
      green_sum = green_sum + pix[j][i][1]
      blue_sum = blue_sum + pix[j][i][2]
      red = float(pix[j][i][0])
      green = float(pix[j][i][1])
      if red + green > most_yellow:
        most_yellow = red + green
      count = count + 1
average_red = red_sum / count
average_green = green_sum / count
average_blue = blue_sum / count
print(average_red)
print(average_green)
print(average_blue)
print(most_yellow)
print(count)
# text=open('C:/python/apple_sweet/Apple_RGB.txt', 'a')
# for i in c:
#   for j in d:
#     if pix[j][i][0] > 0:
#       print(pix[j][i], file=text)
# text.close