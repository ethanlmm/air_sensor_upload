import numpy as np
import os
import re
import csv as CSV
from datetime import datetime

def writeCSV(name,list,postfix=".csv"):
    np.savetxt(name+postfix,list,delimiter=",",fmt="%s")

def readcsv(name,postfix=".csv"):
    np.loadtxt()





root= 'C:/Users/ethan/Documents/workspace/data/'

jpg = '.*\.jpg|.*\.jpeg'
csv = '.*\.csv'
png = '.*\.png'
mat = '.*\.mat'

def list_path(path, type=None):
    if type is None: return [os.path.join(path, name) for name in os.listdir(path)]
    paths = []
    for name in os.listdir(path):
        if (re.match(type, name)):
            paths.append(os.path.join(path, name))
    return paths
def check(str):return re.match(rule,str)

rule=r'(\d+\/+\d+\/+\d*)|(\d+\:+\d*)|[0-9](\.[0-9])?'

def csv_filter(path):
    result=list()
    with open(path, 'r')as fin:
        for row in CSV.reader(fin, delimiter=','):
            row = list(filter(check, row))
            if len(row) != 0:
                arr=str(row[0]).split('/')
                newarr=arr[2]+"-"+arr[0]+"-"+arr[1]

                row[0]=newarr
                result.append(row)
    return result

def time_taged_name(name, format):
    return datetime.now().strftime("%Y-%m-%d_%H_%M") + name + format



