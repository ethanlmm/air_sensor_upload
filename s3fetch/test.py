import os
import re
import csv as CSV
from datetime import datetime
import json
root= 'C:/workspace/work/s3fetch/'

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


def time_taged_name(name, format):
    return datetime.now().strftime("%Y-%m-%d_%H_%M") + name + format

def csv_filter(path,save_path):
    result=list()
    for path in list_path(path):
        with open(path, 'r')as fin:
            for row in CSV.reader(fin, delimiter=','):
                row = list(filter(check, row))
                if len(row) != 0: result.append(row)

    with open(save_path, 'w',newline="") as fout:
        writer = CSV.writer(fout, delimiter=',')
        for row in result:
            writer.writerow(row)

def jsonfy():
    result = list()
    with open(root+'all_data.csv','r') as fin, open(root+'all_data.json','w')as fout:
        result=list()
        for row in CSV.reader(fin, delimiter=','):
            result.append(row)
        json.dump(result,fout)



jsonfy()
