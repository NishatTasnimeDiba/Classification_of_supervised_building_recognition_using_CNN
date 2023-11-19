import cv2
import glob
import os

inputFolder = 'ARResized BANGABANDHU'
os.mkdir('Rotated60 BANGABANDHU')

def rotation(img, angle):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    return img

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    rimg = rotation(image, 60)     
    cv2.imwrite("Rotated60 BANGABANDHU/rimage%04i.jpg" %i, rimg)
    i +=1
    cv2.waitKey(30)
cv2.destroyAllWindows()