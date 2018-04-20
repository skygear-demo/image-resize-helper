
#import skygear
from scipy.misc import imread, imsave, imresize
import urllib.request
import numpy as np

from darkflow.net.build import TFNet
import cv2
import validators


"""using object detection for smart crop"""
options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "bin/tiny-yolo-voc.weights", "threshold": 0.1}


def search_biggest_object(data):
	"""searches bounding box with highest confidence and returns its index
		in the given data, which is a list of dictionaries"""

	length = len(data)
	if length == 0:
		return -1 #no object detected
	else:
		max_index = 0
		max_area = 0 #calculate area to determine which bounding box is the biggest
		area = 0

		for i in range(0, length):
			x_max = data[i]['bottomright']['x'] 
			y_max = data[i]['bottomright']['y']
			x_min = data[i]['topleft']['x']
			y_min = data[i]['topleft']['y']
			area = (x_max - x_min)*(y_max - y_min)
			if area > max_area:
				max_index = i
				max_area = area


	return max_index

#skygear.op('image:smart_resize', user_required=False)
def smart_crop(image): 
	"""crop the image around the most prominent object in the image
	   input is the standard format like jpg or png image"""


	#url check:
	
	if validators.url(image): #if its a valid url
		img = retrieve_url(image)
	else:
		img = cv2.imread(image)
	print(img)
	tfnet = TFNet(options) #load the parameters of the CNN

	data = tfnet.return_predict(img)
	i = search_biggest_object(data)
	x_max = data[i]['bottomright']['x'] ##the labels are misleading
	y_max = data[i]['bottomright']['y']
	x_min = data[i]['topleft']['x']
	y_min = data[i]['topleft']['y']
	
	result_img = img[y_min:y_max,x_min:x_max]
	cv2.imshow("original image", img)
	cv2.imshow("cropped image", result_img)
	cv2.waitKey(0)
	#print(data)
	return result_img

#skygear.op('image:smart_resize', user_required=False)
def keyword_generation(image):
	"""generates words corresponding to the objects in the image
	   input is the standard format like jpg and png image"""

	#url check:
	if validators.url(image): #if its a valid url
		img = retrieve_url(image)
	else:
		img = cv2.imread(image)

	tfnet = TFNet(options) #load the parameters of the CNN
	data = tfnet.return_predict(img)
	keywords = []
	for i in range(0,len(data)):
		keywords.append(data[i]['label'])

	print("list of generated keywords:")
	print(keywords)
	return keywords

"""
=======
import skygear
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plot
from urllib.request import Request, urlopen
import numpy as np
#import io
#import cv2



>>>>>>> 43b99e2238556b290abf8ed398afc79004e20680
# Visit https://<your-endpoint-url>/hello/ to view
@skygear.handler('hello/')
def hello_world(request):
    return 'hello'

#@skygear.op('food:buy', user_required=False)
#def buy_food(food):
#    # TODO: call API about online shopping
#    # return an object to the SDK
#    return {
#        'success': True,
#        'food': food,
#    }

"""

#skygear.op('image:resize', user_required=False)
def resize(image, height = 300, width = 300, auto = True):
	"""resizes the passed image according to the height and width sepcified
	   if auto is true, then resizing is proportional and only height is considered
	   and width is calculated automatically"""
	
	#url check:
	if validators.url(image): #if its a valid url
		img = retrieve_url(image)
	else:
		img = cv2.imread(image)

	#for debugging
	#print(img.shape)

	#error check
	if height > img.shape[0] or width > img.shape[1]:
		print("Error: Specified height and width exceed image dimensions")
		return
	if auto == True:
		ratio = float(height) / img.shape[1]
		width = int(img.shape[0] * ratio)
	resized_img = cv2.resize(img, (height,width))
	print(resized_img.shape)
	cv2.imshow("original image", img)
	cv2.imshow("resized image", resized_img)
	cv2.waitKey(0)
	print("Resizing was successful!")
	return {
		'success': True,
	}



#@skygear.op('image:resize', user_required=False)
def resize_image(image_url, height = 125, width = 125):
	#req = Request(image_url)
	#url_response = urlopen(image_url)
	#img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
	#file = io.StringIO(urlopen(image_url).read())
    img = imread('cute-kittens.jpg')
	#resp = urlopen(image_url)
	#img = np.asarray(bytearray(resp.read()), dtype="uint8")
	#img = cv2.imdecode(img, -1)
    print(img.shape)
    modified_img = imresize(img, (height, width))
    print("Resizing was successful!")
    return {
           'success': True,
        }

	#plot.imshow(img)
	#plot.show()
	#return modified_img


def crop(image, x_min, x_max, y_min, y_max):
	"""function for manual cropping
		origin starts from top left corner of the image
		y increases downwards and x increases leftwards"""

	#url check:
	if validators.url(image): #if its a valid url
		img = retrieve_url(image)
	else:
		img = cv2.imread(image)

	#error check
	if x_min < 0 or y_min < 0 or x_max > img.shape[1] or y_max > img.shape[0]:
		print("Error: Specified height and width exceed image dimensions")
		return

	result_img = img[y_min:y_max, x_min:x_max]
	cv2.imshow("original image", img)
	cv2.imshow("cropped image", result_img)
	cv2.waitKey(0)


def retrieve_url(image_url):
	"""retrieves image from url and decodes it"""
	print("The given url is valid: ")
	url_response = urllib.request.urlopen(image_url)
	img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
	img = cv2.imdecode(img_array, -1)
	#cv2.imshow('URL Image', img)
	#cv2.waitKey(0)

	return img


smart_crop("cute-kittens.jpg")
#smart_crop('http://www.petsworld.in/blog/wp-content/uploads/2014/09/cute-kittens.jpg')
#keyword_generation("../cute-kittens.jpg")


resize_image('http://www.petsworld.in/blog/wp-content/uploads/2014/09/cute-kittens.jpg')

