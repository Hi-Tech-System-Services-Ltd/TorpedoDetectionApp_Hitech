import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from app.digitalCam import *

def test_digitalCam():
    try:
        result_digital = digitalCam()
        if result_digital:
            print(f"digitalCam returned: {result_digital}")
        else:
            print(f"digitalCam returned: {result_digital}")
            
        print("digtalCam is working")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    test_digitalCam()