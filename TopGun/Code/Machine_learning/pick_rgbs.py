from PIL import Image
import numpy as np
import glob
import pandas as pd
import natsort
images = natsort.natsorted(glob.glob('C:/python/apple_sweet/rembg_apples/*.png')) #폴더에 있는 파일들 숫자 순서대로 불러오기
file_count = 0 #불러온 파일 숫자
text=open('C:/python/apple_sweet/Apple_rgbs.txt', 'w')
print("1rd_red, 1rd_r, 1rd_rg, 1rd_most_red, 1rd_least_red, 1rd_most_yellow, 1rd_size, 2nd_red, 2rd_r, 2rd_rg, 2rd_most_red, 2rd_least_red, 2rd_most_yellow, 2nd_size, 3rd_red, 3rd_r, 3rd_rg, 3rd_most_red, 3rd_least_red, 3rd_most_yellow, 3rd_size, 4th_red, 4rd_r, 4rd_rg, 4rd_most_red, 4rd_least_red, 4rd_most_yellow, 4th_size, 5th_red, 5rd_r, 5rd_rg, 5rd_most_red, 5rd_least_red, 5rd_most_yellow, 5th_size, 6th_red, 6rd_r, 6rd_rg, 6rd_most_red, 6rd_least_red, 6rd_most_yellow, 6th_size, height/area", file=text) #특성
for fname in images:
  im = Image.open(fname)
  pix = np.array(im)
  c = np.arange(1,im.size[0],10)
  d = np.arange(1,im.size[1],10)
  red_sum = 0
  green_sum = 0
  blue_sum = 0
  least_red = 0
  most_yellow = 0
  most_red = 0
  count = 0
  file_count = file_count + 1
  for i in c:
    for j in d:
      if pix[j][i][0] > 1:
        red_sum = red_sum + pix[j][i][0]
        green_sum = green_sum + pix[j][i][1]
        blue_sum = blue_sum + pix[j][i][2]
        red = float(pix[j][i][0])
        green = float(pix[j][i][1])
        blue = float(pix[j][i][2])
        if red - green - blue > most_red:
          most_red = round(red - green - blue, 2)
        if red - green - blue < least_red:
          least_red = round(red - green - blue, 2)
        if red + green - blue > most_yellow:
          most_yellow = round(red + green - blue, 2)
        count = count + 1
  average_red = round(red_sum / count, 2)
  average_green = round(green_sum / count, 2)
  average_blue = round(blue_sum / count, 2)
  rg = round(average_red + average_green - average_blue, 2)
  r = round(average_red - average_green - average_blue, 2)
  if file_count % 6 == 1:
    print(average_red, file=text, end =', ')
    # print(average_green, file=text, end =', ')
    # print(average_blue, file=text, end =', ')
    print(r, file=text, end =', ')
    print(rg, file=text, end =', ')  
    print(most_red, file=text, end =', ')
    print(least_red, file=text, end =', ')
    print(most_yellow, file=text, end =', ')
    print(count, file=text, end =', ')
    area = count
  elif file_count % 6 == 0:
    print(average_red, file=text, end =', ')
    # print(average_green, file=text, end =', ')
    # print(average_blue, file=text, end =', ')
    print(r, file=text, end =', ')
    print(rg, file=text, end =', ')
    print(most_red, file=text, end =', ')
    print(least_red, file=text, end =', ')
    print(most_yellow, file=text, end =', ')
    print(count, file=text, end =', ')
    print(count/area, file=text)
  else:
    print(average_red, file=text, end =', ')
    # print(average_green, file=text, end =', ')
    # print(average_blue, file=text, end =', ')
    print(r, file=text, end =', ')
    print(rg, file=text, end =', ')
    print(most_red, file=text, end =', ')
    print(least_red, file=text, end =', ')
    print(most_yellow, file=text, end =', ')
    print(count, file=text, end = ', ')
text.close