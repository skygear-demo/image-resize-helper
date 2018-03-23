import skygear
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plot
from urllib.request import Request, urlopen
import numpy as np
#import io
#import cv2



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


@skygear.op('image:resize', user_required=False)
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
    print("Resizing was successful!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return {
           'success': True,
        }
	#plot.imshow(img)
	#plot.show()
	#return modified_img


resize_image('http://www.petsworld.in/blog/wp-content/uploads/2014/09/cute-kittens.jpg')
