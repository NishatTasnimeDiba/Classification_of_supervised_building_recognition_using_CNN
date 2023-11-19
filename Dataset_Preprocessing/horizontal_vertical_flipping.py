import cv2
import glob
import os

inputFolder = 'BANGABANDHU'
os.mkdir('HV Flipped BANGABANDHU')

def vertical_flip(image, flag):
       if flag:
           return cv2.flip(image, 1)
       else:
           return image
       
def horizontal_flip(image, flag):
       if flag:
           return cv2.flip(image, 1)
       else:
           return image
       
       

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    himg = horizontal_flip(image, True)
    cv2.imwrite("HV Flipped BANGABANDHU/himage%04i.jpg" %i, himg)
    vimg = vertical_flip(image, True)
    cv2.imwrite("HV Flipped BANGABANDHU/vimage%04i.jpg" %i, vimg)
    i +=1
    cv2.waitKey(30)

cv2.destroyAllWindows()

