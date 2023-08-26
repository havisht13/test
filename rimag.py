import os
import PIL
from rembg import remove
from PIL import Image


foder_image ='/home/havisht/PETbenny/Libray/image/downurl/'
output_path = '/home/havisht/PETbenny/Libray/image/kbackgrand/'
num = 0
for one_image in os.listdir(foder_image):
    num+=1
    print(one_image)
    inputt = PIL.Image.open(foder_image + one_image)
    print("===========Open Image=============")
    output = remove(inputt)
    print("===========REMOVER BACKGRAND======")
    output.save(output_path+one_image)
    print("=======Save Remove image", num)

