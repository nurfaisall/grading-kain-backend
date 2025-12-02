import pandas as pd
import os
from dotenv import load_dotenv
from openpyxl import load_workbook
import xlwings as xw

load_dotenv()

def get_db():
    file_path = os.environ.get("DB_PATH")
    wb = load_workbook(file_path, read_only=True)
    # ws = wb["db_zb"]
    wb_zb = wb['db_zb']
    wb_zb = wb_zb.tables['Table 1'].ref


    print(wb_zb)
    
    

    return
get_db()