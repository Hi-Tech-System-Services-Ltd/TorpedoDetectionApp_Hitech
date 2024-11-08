
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))


from imports import *
from components.clsTorpedo import *

model_path = "models\\digitalcam_cls.pt"
image_path = "images\\digital_image.jpg"

def test_clsTorpedo():
    try:
        isTorpedo = clsTorpedo(clsModePath=model_path, imagePath=image_path)
        print(isTorpedo)
        if isTorpedo:
            print("Inside If")
        else:
            print("Inside Else")         
        print("clsTorpedo is Working")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_clsTorpedo()