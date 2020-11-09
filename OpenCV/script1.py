import cv2

img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)

resized_image = cv2.resize(img,(500,1000))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resize.jpg",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

'''
to resize all images to 100x100
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
'''
