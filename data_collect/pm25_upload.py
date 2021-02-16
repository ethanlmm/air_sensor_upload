import boto3
from config import *
import os

root=os.path

save_root=root
BUCKET = "pm2.5"
s3_root=""
dump=s3_root+"data/"

def upload(From,To):
    s3 = boto3.resource('s3')
    for name in os.listdir(From):
        print('uploading ',name)
        s3.Bucket(BUCKET).upload_file(From+name, To+name)
        print('DONE')
    print('*---------------UPLOAD FINISH------------------*')
#upload(save_root,dump)