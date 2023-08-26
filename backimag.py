import os
import PIL
from PIL import Image

end_image = '/home/havisht/PETbenny/Libray/image/endimag/'
unbk_image = '/home/havisht/PETbenny/Libray/image/kbackgrand/'

back_image = '/home/havisht/PETbenny/Libray/image/30darsad.png'


num = 0 

for one_image in os.listdir(unbk_image):
    num += 1
    print("------------",num,"-------------------")
    print(one_image)
    frontImage = Image.open(unbk_image + one_image)
    backImage = Image.open(back_image)
    frontImage = frontImage.convert("RGBA")
    background = backImage.convert("RGBA")
    width = (background.width - frontImage.width) // 2
    height = (background.height - frontImage.height) // 2
    background.paste(frontImage, (width, height), frontImage)
    print("===Change back image===")
    background.save(end_image + one_image, format="webp")
    print("Save Image with format WEBP")

