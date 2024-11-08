
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def saveImage(src, dst_path, filename):
    try:
        dst = os.path.join(dst_path, filename)

        shutil.copy2(src, dst)
        print(f"Image saved to {dst}")
        
    except Exception as e:
        print(f"Error: {e}")
        