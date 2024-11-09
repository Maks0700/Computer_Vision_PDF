from loguru import logger
from Converter_Class import Converter_Pdf_Png
import sys
import os
from Module_Database import create_db



#create logs
logger.add("Logs.log",format="{time} {level} {message}",
           level="DEBUG",rotation="10 KB",compression="zip")

@logger.catch# отлавливаем все исключения при дебаге
def main_call():
    converter=Converter_Pdf_Png()
    converter.__convert_pdf_png__()
    
    if len(sys.argv)>1:
        name=sys.argv[1]
    else:
        name=input("Введите имя Базы данных: ")
        while f"{name}.accdb" in os.listdir(os.getcwd()):
            name=input("Такое имя уже существует. Введите другое имя Базы данных: ")
        
            
            
    create_db(name=name,**converter.__reader_png_to_text__())


if __name__=="__main__":
   main_call()
    
    
    
    




    
    
    

    
    
    
        
        









        



    


    

    

        
    
     






