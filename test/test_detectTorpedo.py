
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components.detectTorpedo import *

model_path = "models\\cam2_detect.pt"
image_path = "testing_images\\cam2.jpg"

def test_detectTorpedo():
    try:
        x1, y1, x2, y2 = detectTorpedo(model_path, image_path)
        
        if x1 == None:
            print("Detect Torpdeo Returned None")
        else:
            image = cv2.imread(image_path)
            cv2.rectangle(image, (x1, y1), (x2, y2), color=(255, 255, 255), thickness=2)
            
            cv2.imshow('Result', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            print("detectTorpedo is working")   
            
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_detectTorpedo()