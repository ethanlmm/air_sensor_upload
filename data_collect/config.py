from datetime import timedelta
#streaming capture config
admin_password='admin:admin'
address='@192.168.1.30:554/'
stream='video.pro1'
url = 'rtsp://'+admin_password+address+stream

#timer config
cut_interval=timedelta(minutes=10)
delete_interval=timedelta(days=1)



#path of video save and upload
root=''
save_root=root+'save/'
BUCKET = "cameratest1"
s3_root="C:/root_of_sensor_and_camera/data_collect/"
dump=s3_root+"dump/"





