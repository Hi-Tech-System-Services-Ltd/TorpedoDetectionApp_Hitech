
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components.saveImage import *

src = "testing_images\cam1.jpg"
dst_path = "images"
filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

def test_saveImage():
    try:
        saveImage(src, dst_path, filename)
        print("saveImage is working")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_saveImage()