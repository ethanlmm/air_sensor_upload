import cv2

def video_capture(video_writer,url,timer):
    cap = cv2.VideoCapture(url)
    while(cap.isOpened() and timer()):
        for x in range(100):
            ret, frame = cap.read()
            if ret==True:
                frame = cv2.flip(frame,0)
                # write the flipped frame
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                video_writer.write(frame)
            else:
                cap.release()
                video_writer.release()
                return
    cap.release()
    video_writer.release()

def video_writer(path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    return cv2.VideoWriter(path, fourcc, 30, (1920, 1080))





