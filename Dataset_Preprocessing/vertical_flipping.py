import cv2
import glob
import os

inputFolder = 'BANGABANDHU'
outputFolder = 'V Flipped BANGABANDHU'

os.mkdir(outputFolder)

def vertical_flip(image, flag):
    if flag:
        return cv2.flip(image, 0)  # 0 indicates vertical flip
    else:
        return image

i = 0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    nimg = vertical_flip(image, True)
    cv2.imwrite(f"{outputFolder}/image{str(i).zfill(4)}.jpg", nimg)

    i += 1
    cv2.imshow('image', nimg)
    cv2.waitKey(30)

cv2.destroyAllWindows()
