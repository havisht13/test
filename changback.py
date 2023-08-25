import os
import PIL
from rembg import remove
from PIL import Image

nameimage = 'G:\hackPetpars\Libray\image\downurl\\'
output_path = 'G:\hackPetpars\Libray\image\kbackgrand\\'
num = 0
image = os.listdir(nameimage)
print(image)
for im in image:
    num+= 1
    inputt = PIL.Image.open(nameimage+im)
    output = remove(inputt)
    output.save(output_path+im)
    print("REMOVE BACKGRAND : ", num)
    
#endimage = "G:\hackPetpars\Libray\image\endimag\ " + nameima
#unbac = "G:\hackPetpars\Libray\image\kbackgrand\ " + nameima
#backimage = '31darsad.png'
#frontImage = Image.open(unbac)
#background = Image.open(backimage)
#frontImage = frontImage.convert("RGBA")
#background = background.convert("RGBA")
#width = (background.width - frontImage.width) // 2
#height = (background.height - frontImage.height) // 2
#background.paste(frontImage, (width, height), frontImage)
#background.save(endimage, format="png")
#print("change backgrand : ",nameima)

#image = Image.open(endimage)
#image = image.convert('RGB')
#namewebp = "Libray\image\endimag\ " + str(name_image) + ".webp"
#image.save(namewebp, 'webp')
#print("Save image WEBP")
