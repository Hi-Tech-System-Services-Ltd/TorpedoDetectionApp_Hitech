import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from components.calculateBBoxInfo import *

def test_calculateBBoxInfo(x1, y1, x2, y2):
    try:
        c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
        
        print(f"Center_x: {c_x}\nCenter_y: {c_y}\nWidth: {w}\nHeight; {h}")
        print("calculateBBox is working")
        
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == '__main__':
    test_calculateBBoxInfo(10, 10, 20, 20)