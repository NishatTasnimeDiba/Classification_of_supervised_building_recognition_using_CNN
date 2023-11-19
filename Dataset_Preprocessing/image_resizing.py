import cv2
import glob
import os


inputFolder = 'WELDING SHOP'
os.mkdir('ARResized WELDING SHOP')


def resize_image_with_aspect_ratio(image, max_width, max_height):
    height, width = image.shape[:2]
    aspect_ratio = float(width) / float(height)

    new_width = min(max_width, int(max_height * aspect_ratio))
    new_height = min(max_height, int(max_width / aspect_ratio))
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    
    return resized_image

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    sized_image = resize_image_with_aspect_ratio(image, max_width=800, max_height=600)
    cv2.imwrite("ARResized WELDING SHOP/rimage%04i.jpg" %i, sized_image)
    i +=1
    cv2.waitKey(30)
cv2.destroyAllWindows()