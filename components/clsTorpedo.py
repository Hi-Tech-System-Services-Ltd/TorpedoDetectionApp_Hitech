
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def detectTorpedo(detectModelPath, imagePath):
    detectModel = YOLO(detectModelPath)
    
    results = detectModel(imagePath)
    
    if not results:
        print("No bounding box")
        return -99, -99, -99, -99
    
    for result in results:
        boxes = result.boxes
        if not boxes:
            print("No boxes found")
            return -99, -99, -99, -99
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().astype(int)
            return x1, y1, x2, y2
    
    return -99, -99, -99, -99
