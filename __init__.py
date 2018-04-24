import skygear
from scipy.misc import imread, imsave, imresize
from urllib.request import Request, urlopen
import numpy as np
from skygear.utils.assets import directory_assets
from skygear.container import SkygearContainer
from skygear.options import options # to obtain the master key
import io
from PIL import Image
import requests


master_container = SkygearContainer(
    api_key='6d8edfb22a2a48d3b5c63c773dc46761'
)

def upload_image_to_skygear(bytes_data, filename, content_type):
	host = 'https://imageprocessing.skygeario.com/'
	asset_name = filename
	api_key = '22aaa3c73b9249b6b838c0369ac06118'
	headers = {
        'Accept': 'application/json',
        'Content-Type': content_type,
        'X-Skygear-API-Key': api_key,
	}
	url = host + '/files/' + asset_name
	response = requests.request(
        'PUT',
        url,
        data=bytes_data,
        headers=headers,
	)
	json_body = response.json()
	print(json_body)
	"""
	output_name = json_body['result']['$name']
	return output_name
	"""




# Visit https://<your-endpoint-url>/hello/ to view



@skygear.handler('hello/')
def hello_world(request):
    return 'hello'



@skygear.op('image:resize', user_required=False)
def resize_image(image_url="", height = 125, width = 125):
    img = Image.open('cute-kittens.jpg')
    global count

    #print(img.shape)
    output_image = img.resize((width,height))
    print("Resizing was successful!")
    #imsave('./temp/image'+str(count)+'.png', modified_img)
    #count = count + 1;
    memory_file = io.BytesIO()
    output_image.save(memory_file, format='JPEG')

    asset_name = upload_image_to_skygear(
		memory_file.getvalue(),
		'image.jpg',
		'image/jpeg',
		)
    print(asset_name)
    return asset_name

"""
	return {
           'success': True,
           url:""
        }
"""
resize_image('http://www.petsworld.in/blog/wp-content/uploads/2014/09/cute-kittens.jpg')
