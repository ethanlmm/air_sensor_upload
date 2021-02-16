from datetime import datetime,timedelta
import os
import re
def timer(time):
    if isinstance(time,datetime): futuretime=time
    elif isinstance(time,timedelta): futuretime=datetime.now()+time
    else: return
    def check():
        return datetime.now()<futuretime
    return check

def time_taged_name(name,format):
    return datetime.now().strftime("%Y-%m-%d_%H_%M")+name+format


jpg = '.*\.jpg|.*\.jpeg'
csv = '.*\.csv'
png = '.*\.png'
mat = '.*\.mat'
avi = '.*\.avi'


def list_path(path, type=None):
    if type is None: return [os.path.join(path, name) for name in os.listdir(path)]
    paths = []
    for name in os.listdir(path):
        if (re.match(type, name)):
            paths.append(os.path.join(path, name))
    return paths