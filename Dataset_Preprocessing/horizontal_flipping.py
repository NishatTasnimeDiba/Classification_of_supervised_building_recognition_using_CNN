import cv2
import glob
import os

inputFolder = 'BANGABANDHU'
os.mkdir('H Flipped BANGABANDHU')

def horizontal_flip(image, flag):
       if flag:
           return cv2.flip(image, 1)
       else:
           return image

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    nimg = horizontal_flip(image, True)
    cv2.imwrite("H Flipped BANGABANDHU/image%04i.jpg" %i, nimg)

    i +=1
    cv2.imshow('image', nimg)
    cv2.waitKey(30)

cv2.destroyAllWindows()