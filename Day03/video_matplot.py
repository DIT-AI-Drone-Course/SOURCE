import cv2
from matplotlib import pyplot as plt

img = cv2.imread('drone01.jpeg', cv2.IMREAD_COLOR)

# BGR -> RGB
b, g, r = cv2.split(img)
image2 =cv2.merge([r,g,b])

plt.imshow(image2)
plt.xticks([]) # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()