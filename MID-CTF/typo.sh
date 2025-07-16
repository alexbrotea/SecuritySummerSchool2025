from PIL import Image
import numpy as np
import requests
from io import BytesIO

url = 'http://141.85.224.118:8080/history/nebuchadnezzar-ii.jpg'
response = requests.get(url)
im = Image.open(BytesIO(response.content)).convert('L')

arr = np.array(im)
bit = (arr >> 2) & 1

vis = (bit * 255).astype(np.uint8)
Image.fromarray(vis).save('bit2.png')
