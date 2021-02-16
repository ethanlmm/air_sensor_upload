import boto3
from config import *
import os

def upload(From,To):
    s3 = boto3.resource('s3')
    for name in os.listdir(From):
        print('uploading ',name)
        s3.Bucket(BUCKET).upload_file(From+name, To+name)
        print('DONE')
    print('*---------------UPLOAD FINISH------------------*')
upload(save_root,dump)