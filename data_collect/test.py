
from util import *
from datetime import timedelta
import time
'''bucket_name='cameratest1'


s3 = boto3.resource('s3')
BUCKET = "cameratest1"

s3.Bucket(BUCKET).upload_file("README.txt", "dump/README.txt")'''


x=datetime.now()
y=timedelta(minutes=1)
y_timer=timer(y)
x=datetime.now()+timedelta(minutes=1)

x_timer=timer(x)

x_timer()
y_timer()