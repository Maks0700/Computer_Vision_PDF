import os
import glob
from easyocr import Reader
import re

class Variable_Function:
    
    output_pdf =f"{os.getcwd()}"
    list_photo=glob.glob("**/*.pdf",recursive=True)
    data_empty=dict.fromkeys(list_photo)
    reader=Reader(["ru"],gpu=True)
    


    
    
        
        
        
        
    
   




    




# test1="asasasasaqqfc91023445"
# test2="013344"
# test3="900978112s"
# print(test1.isdigit())
# print(test2.isdigit())
# print(test3.isdigit())