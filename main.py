# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import shutil  # برای دانلود عکس
from rembg import remove
from PIL import Image

import pandas as pd
import os

from openpyxl import load_workbook
import xlsxwriter
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class PetShop:

    def ALink(self):
        links = set()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        result = requests.get(self, headers=headers)
        if result.status_code==200:
            page = BeautifulSoup(result.text, 'html.parser')
            print("yes")
        for element in page.find_all('a'):
            link = element.get('href')
            if not link:
                continue
            if link.find("/product/") == -1:
                continue
            links.add(link)
        return links

    def DownloderImage(self , name_image):
        # دانلود عکس‌ها از لینک مورد نظر
        imagelink = self
        #print("image link : ", imagelink)
        nameima = str(name_image + ".png")
        nameimage = f'\hackPetpars\Libray\image\downurl\{nameima}'
        print("============", nameimage)

        print("name image : ", nameima)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        res = requests.get(imagelink, headers=headers,stream=True )
        if res.status_code == 200:
            with open(nameimage, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', nameimage)
        else:
            print('Image Couldn\'t be retrieved')

    def base_url(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        result = requests.get(self, headers=headers)
        if result.status_code==200:
            target_page = BeautifulSoup(result.text, 'html.parser')
        product_name = target_page.find('h1', class_='product_title').text.replace("|", ' ')
        #details_short = target_page.find('div', class_="woocommerce-product-details__short-description")\
        #    .text.replace('\n', " ")
        details_long = target_page.find(class_="woocommerce-Tabs-panel").find("p").text
        image = target_page.find('div', class_="woocommerce-product-gallery__image")
        # اینجا لینک دانلود عکس از سابت در ةوردیم
        for Imageulr in image.find_all('a'):
            Imagehref = Imageulr.get('href')
            if not Imagehref:
                continue
            imagelink = Imagehref
            PetShop.DownloderImage(imagelink, product_name)
            #pathimage = "Libray\image\endimag\"
            pathimage = product_name + ".webp"
            #print(pathimage)
        DataUrl = [product_name,details_long,pathimage]
        raw_data = ["name", "long", "image"]
        res = {raw_data[a]:DataUrl[a] for a in range(len(raw_data))}
        return res

    def save_file(self):
        namexlsx = 'hapydog.xlsx'
        # create excel file if it does not exist
        if not os.path.isfile(namexlsx):
            df = pd.DataFrame(data=self, index=[1])
            df.to_excel(namexlsx, index=False)
            print("Dictionary converted into excel...")

        df1 = pd.read_excel(namexlsx)
        df2 = pd.DataFrame(self,index=[0], columns=["name","long","image"])
        df3 = pd.concat([df1, df2])
        df3.to_excel(namexlsx, index=False)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #link = 'https://petpars.com/yith_product_brand/happydog/'
    siteT = str(input("Enter Url site :"))
    my_links = PetShop.ALink(siteT)  # لینک محصصولات در این متغییر میفرستیم
    mylist = []  # اطلاعات لینک ها در یک لیست به صورت دیگشنری ذخیزه میکنیم
    num = 0
    for elemet in my_links:
        num += 1
        onelink = PetShop.base_url(elemet)
        mylist.append(onelink)
        print(onelink)
        save = PetShop.save_file(onelink)
        print("=======>>Save excel Done<<========", num, "_", save)
        print(mylist)
        print("===================END", num, "=========================")

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
