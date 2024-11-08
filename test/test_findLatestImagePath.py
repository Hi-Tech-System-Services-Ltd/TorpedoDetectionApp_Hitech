
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components.findLatestImagePath import *

dir_path = "images"

def test_findLatestImagePath():
    try:
        name = findLatestImagePath(dir_path)
        print(f"Path: {name}")
        print("findLatestImagePath is working")
    except Exception as e:
        print(f"Exception: {e}")



if __name__ == "__main__":
    test_findLatestImagePath()