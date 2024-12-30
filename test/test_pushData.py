
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from database.pushData import *


def test_saveImage():
    try:
        print("Testing Push Data API")
        pushData_API(99, 300, 300, 150, 75, 99, "2000-00-00 00-00-00.jpg")
        print("Push Data API is working")
    except Exception as e:
        print(f"Exception: {e}")

    # try:
    #     print("Testing pushData ")
    #     pushData(99, 99, 99, 99, 99, 99, 99)
    #     print("pushData  is working")
    # except Exception as e:
    #     print(f"Exception: {e}")

if __name__ == "__main__":
    test_saveImage()
