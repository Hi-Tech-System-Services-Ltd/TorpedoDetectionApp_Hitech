
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from components.deleteFiles import *

dir_path = "images"

def test_deleteFiles():
    try:
        deleteFiles(dir_path)
        print("files deleted")
        print("deleteFiles is working")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    test_deleteFiles()