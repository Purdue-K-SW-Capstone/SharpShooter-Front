from skimage import io, color
import natsort
import glob
import numpy as np

rgba = io.imread('C:/python/apple_sweet/nukki_apples/1-1.png')
print(rgba)
rgb = np.delete(rgba, 3 , axis = 1)
lab = color.rgb2lab(rgb)
print(lab)

# images = natsort.natsorted(glob.glob('C:/python/apple_sweet/nukki_apples/*.png')) #폴더에 있는 파일들 숫자 순서대로 불러오기
# for fname in images:
#   rgb = io.imread(fname)
#   lab = color.rgb2lab(rgb)
#   print(lab)
