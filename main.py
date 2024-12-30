
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from app.cam1 import *
from app.cam2 import *
from app.cam3 import *
from components.findLatestImageName import *
from database.pushData import *

# replace it with code for ocr / number detection
torpedo_id = 55 

images_cam1 = "images_cam1"
images_cam2 = "images_cam2"
images_cam3 = "images_cam3"

def cam1_thread_func():
    cam_id = 1
    result = cam1()
    
    if result is None:
        print("Cam1: No Detection or an error occurred in cam1 function.")
    else:
        c_x, c_y, w, h = result
        filename = findLatestImageName(images_cam1)
        pushData_API(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print("Cam1-data_pushed")

def cam2_thread_func():
    cam_id = 2
    result = cam2()
    
    if result is None:
        print("Cam2: No Detection or an error occurred in cam2 function.")
    else:
        c_x, c_y, w, h = result
        filename = findLatestImageName(images_cam2)
        pushData_API(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print("Cam2-data_pushed")


def cam3_thread_func():
    cam_id = 3
    result = cam3()
    
    if result is None:
        print("Cam3 No Detection or an error occurred in cam3 function.")
    else:
        c_x, c_y, w, h = result
        filename = findLatestImageName(images_cam3)
        pushData_API(torpedo_id, c_x, c_y, w, h, cam_id, filename)
        print("Cam3-data_pushed")


def main():
    # cam1_thread = threading.Thread(target=cam1_thread_func, daemon=True)
    # cam2_thread = threading.Thread(target=cam2_thread_func, daemon=True)
    # cam3_thread = threading.Thread(target=cam3_thread_func, daemon=True)

    # cam1_thread.start()
    # cam2_thread.start()
    # cam3_thread.start()

    # cam1_thread.join()
    # cam2_thread.join()
    # cam3_thread.join()
    
    
    try:
        while True:
            cam1_thread = threading.Thread(target=cam1_thread_func, daemon=True)
            cam2_thread = threading.Thread(target=cam2_thread_func, daemon=True)
            cam3_thread = threading.Thread(target=cam3_thread_func, daemon=True)

            cam1_thread.start()
            cam2_thread.start()
            cam3_thread.start()

            cam1_thread.join()
            cam2_thread.join()
            cam3_thread.join()

            gc.collect()

            time.sleep(1)

    except Exception as e:
        print(f"Exception: {e}")
       
    

if __name__ == "__main__":
    main()
