import PIL, os
from PIL import Image

os.chdir('/home/entong/Pictures/') # change to directory where image is located

picture= Image.open('life.jpg')

picture.rotate(90).save('life_rotated123.png')
