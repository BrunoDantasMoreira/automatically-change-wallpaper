# Import all necesary libraries
import cv2
import os 
import time

def screenshot(video):
    
    # Read the video from specified path
    cam = cv2.VideoCapture('video')
    intvl = 2 #interval in second(s)
    fps = int(cam.get(cv2.CAP_PROP_FPS))
    currentFrame = 0
    
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    
    except OSError:
        print('Error: Creating directory of data')
    
    print("fps: ", fps)
    
    while True:
        ret, frame = cam.read()
        if ret:
            if(currentFrame % (fps*intvl) == 0):
                name = './data/frame' + str(currentFrame) + '.jpg'
                print('Creating... ', name)
                cv2.imwrite(name, frame)
            currentFrame += 1
    
        else:
            break
    
    cam.release()
    cv2.destroyAllWindows()


