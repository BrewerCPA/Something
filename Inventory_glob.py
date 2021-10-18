# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:38:35 2021

@author: chase
"""

import calendar
import glob
import re



path = r'C:\Users\chase\OneDrive\Desktop\Balance Sheet\Inventory\Ekos Inventory Analysis\Ekos Inv Downloads\[0-9]*.[0-9]*'

def get_files(path): 
    files = glob.glob(path)
    
    return files


def file_dates(file):
    year = int(re.search(r'(\d+)', file).group())
    month = int(re.search(r'\.(\d\d)', file).group()[1:])
    day = calendar.monthrange(year, month)[1]
       
    return year, month, day
        