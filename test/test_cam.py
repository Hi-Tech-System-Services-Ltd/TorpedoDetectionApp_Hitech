import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from app.cam1 import *

def test_cam1():
    try:
        c_x, c_y, w, h = cam1()
        
        if c_x == -99:
            print("No Detection")
        else:
            print(f"Center_x: {c_x}\nCenter_y: {c_y}\nWidth: {w}\nHeight: {h}")
            
        print('Cam1 is working')
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_cam1()