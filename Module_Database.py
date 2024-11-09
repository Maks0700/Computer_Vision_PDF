from contextlib import suppress
from PIL import Image
import io
import pyodbc as pd
import os
from collections import deque
import win32com.client
from pyodbc import ProgrammingError
from pywintypes import com_error
import pypyodbc
import re
from comtypes.client import CreateObject
import msaccessdb


def create_db(name:str,**data):
    database_path=f"{os.getcwd()}\{name}.accdb"
    conn_str=(f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={os.getcwd()}\{name}.accdb;")
    msaccessdb.create(database_path)
    
    
    
    conn_database=pd.connect(conn_str)
    cursor=conn_database.cursor()
    
    cursor.execute("""CREATE TABLE users (name TEXT, number_document TEXT)""")
    
    for key,value in data.items():
        name=re.search(r"\\([^\\]+)\.jpg",key).group(1)
        cursor.execute("INSERT INTO users (name, number_document) VALUES (?, ?)",(name,value))
    
    conn_database.commit()
    cursor.close()
    conn_database.close()
    

    