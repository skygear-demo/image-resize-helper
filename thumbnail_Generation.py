from scipy.misc import imread, imsave, imresize
import os
import matplotlib.pyplot as plot

def resize(image_path, height = 125, width = 125):
	img = imread(image_path)
	print(img.dtype,img.shape)
	modified_img = imresize(img, (height, width))
	cwd = os.getcwd()
	imsave(cwd+'/resized_image.jpg', modified_img)
	return modified_img
"""
image1 = imread('windmills.png')
print(image1.dtype, image1.shape)
plot.imshow(image1)
plot.show()
"""
img = resize('windmills.png')
plot.imshow(img)
plot.show()
