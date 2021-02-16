from util import *
from video_process import *
import shutil
import os
from config import *
import time


def main():
    delete_timer = timer(delete_interval)
    print('Start Recording')
    while(True):
        cut_timer=timer(cut_interval)
        #video writer setup
        name=time_taged_name('NAME01','.avi')
        path=root+name
        writer=video_writer(path)
    
        #streaming video capture
        video_capture(writer,url,cut_timer)
        print('video capture finished')

        #save
        save_path=save_root+name
        print('move to',save_path)
        shutil.move(path,save_path)

        if False and delete_timer():
            shutil.rmtree(save_root)
            time.sleep(5)
            os.mkdir(save_root)
            delete_timer = timer(timedelta(days=1))
main()
