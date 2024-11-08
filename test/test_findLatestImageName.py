
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components.findLatestImageName import *

dir_path = "images"

def test_findLatestImageName():
    try:
        name = findLatestImageName(dir_path)
        print(f"Name: {name}")
        print("findLatestImageName is working")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_findLatestImageName()