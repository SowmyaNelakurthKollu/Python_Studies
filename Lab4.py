import skimage
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from skimage.color import rgb2gray
from skimage import io
from skimage.filters import threshold_otsu
from skimage.filters.rank import threshold
from skimage.transform import rescale, resize
from skimage.exposure import histogram
from skimage.util import img_as_ubyte

filename_path = '/Users/SowmyaN/PycharmProjects/Assignments'
filename = os.path.join(filename_path,'coins.jpg')


image = io.imread(filename)

print('----------Task 1----------')
print(image.shape)
print(image.dtype)
print(image[1,100])

io.imshow(image)
io.show()

ax = plt.imshow(image)
plt.show()


print('----------Task 2----------')


filename_path = '/Users/SowmyaN/PycharmProjects/Assignments'
filename2 = os.path.join(filename_path,'astronaut.jpg')

image2 = io.imread(filename2)
print(image2.shape)
print(image2.dtype)
print(image2[1,100,1])
grayscale = rgb2gray(image2)

io.imshow(grayscale)
io.show()

print(grayscale.shape)
print(grayscale.dtype)

print(grayscale[1,100])
print('----------Task 3----------')

image_rescaled = rescale(grayscale,0.25, anti_aliasing=False)
image_resized=resize(grayscale, (image2.shape[0] // 4, image2.shape[1]// 4),
anti_aliasing=True)
io.imshow(image_rescaled)
io.show()
io.imshow(image_resized)
io.show()

print('----------Task 4----------')
print(grayscale[1])
ax = plt.hist(grayscale.ravel(), bins = 256)
t =threshold_otsu(grayscale)
binary = grayscale < t
fig, ax = plt.subplots()
plt.imshow(binary, cmap="gray")
plt.show()


