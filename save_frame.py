# Import all necesary libraries
import cv2
import os 
from PIL import Image
import numpy as np

def screenshot(video):
    
    cam = cv2.VideoCapture(video)
    if not cam.isOpened():
        print("Error: Unable to open video.")
        exit()

    intvl = 3 #interval in second(s)
    fps = int(cam.get(cv2.CAP_PROP_FPS))
    currentFrame = 500
    index = 3058
    all_prints = []
    
    try:
        if not os.path.exists(r'C:\Users\Dell\Pictures\WallPapers\data'):
            os.makedirs(r'C:\Users\Dell\Pictures\WallPapers\data')
    
    except OSError:
        print('Error: Creating directory of data')
    
    print("fps: ", fps)
    
    while True:
        ret, frame = cam.read()
        if ret:
            if(currentFrame % (fps*intvl) == 0):
                name = fr'C:\Users\Dell\Pictures\WallPapers\data\frame{str(index)}.jpg'
                print('Creating... ', name)

                # Cropping the image to get rid of the black bar
                pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                box = (0, 90, 1220, 630)
                cropped_img = pil_img.crop(box)
                cropped_frame = cv2.cvtColor(np.array(cropped_img), cv2.COLOR_RGB2BGR)

                # Saving 
                cv2.imwrite(name, cropped_frame)

                index += 1
                all_prints.append(name)
                with open(r'D:\Codes\Python\automatically-change-wallpaper\prints.txt', 'a') as txt:
                    print('Creating... ', name)
                    txt.write(f'{name}\n')

            currentFrame += 1
    
        else:
            break
    
    cam.release()
    cv2.destroyAllWindows()

    return all_prints


