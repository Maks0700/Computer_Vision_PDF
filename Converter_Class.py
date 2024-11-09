from contextlib import suppress
import io
from PIL import Image,ImageEnhance
import glob
import os
import aspose.pdf as ap
import re
from easyocr import Reader
import numpy
from Variables_Extra import Variable_Function
from Module_Database import create_db
import shutil





class Computer_Vision:
        
    def __reader_pdf_file__(self,filename:str)->str:
        
        if os.path.isfile(filename):
            
            document=ap.Document(filename)#read the document by filepath
            resolution=ap.devices.Resolution(500)#create a resolution object with 500 DPI   
            device=ap.devices.PngDevice(resolution)#create object for converter
            
            #Отделение кода здесь для того чтобы первая часть подготовила изображение и настроила к обработке
            # а вторая часть будет вываодить изображение по пути указанному
            filename_without_ext=re.search(r"(.+)\.pdf",filename).group(1)
            output_path=os.path.join(os.getcwd(),f"{filename_without_ext}.jpg")
            image_stream=io.FileIO(
                output_path, "x")
            data=device.process(document.pages[1],image_stream)#total processing document
            image_stream.close()
        
        else:
            return "File not found"
        
    #make to convert pdf into jpg
    def convert_pdf_png(self):
        
        os.makedirs(name="c:\\Удаленные_PDF",exist_ok=True)#create the folder with parametr not unique name in catalog     
        if Variable_Function.list_photo:
            for item in Variable_Function.list_photo:
                with suppress(FileExistsError):
                    converter_item=self.__reader_pdf_file__(item)
                
                if re.search(r"\\([^\\]+)",item).group(1) not in os.listdir("c:\\Удаленные_PDF"):
                    shutil.move(os.path.abspath(item),"c:\\Удаленные_PDF")#add to folder image in order to save pdf file
                else:
                    os.remove(item)
                    
    #Превращаем нашу фотку в серый цвет для лучшего распознавания номера дока
    def __color_to__gray(self,file):
        
           file_total=Image.open(file,"r")
           gray_image=ImageEnhance.Color(file_total).enhance(0.0)
           bw_image=gray_image.convert("L")
           bw_image.save(file)
    
    def __check_is_digit__(self,parametr): #logic function for for found digit 
        return True if (parametr.isdigit() and len(parametr) in range(6,8)) else False
    
    def __check_is_digit_regex(sefl,parametr):#The same function as previous but with regular expressions
        return True if (re.search(r"[~#&\d] (\d{6,7})",parametr)) else False
    

    def reader_png_to_text__(self):
        
        dict_total={}
        for key in glob.glob("**\*.jpg"):
                self.__color_to__gray(key)
                img=numpy.array(Image.open(key,"r"))# open image as array in order to avoid  exception with russian symbols in file_path
                
                context_text_key=((Variable_Function.reader.readtext(img,detail=0)))#read content of *.jpg file in view text
               
                for item in context_text_key:
                    if self.__check_is_digit__(item):
                        dict_total[key]=item
                        
                    elif self.__check_is_digit_regex(item):
                        dict_total[key]=re.search(r"[~#&\d] (\d{6,7})",item).group(1)
                        
                    

                    
        dict_total_res={
                key:value for key,value in sorted(dict_total.items(),
                key=lambda item:item[1])
                }
        return dict_total_res
