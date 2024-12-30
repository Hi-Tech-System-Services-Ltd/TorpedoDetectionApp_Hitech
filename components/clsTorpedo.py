import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def clsTorpedo(clsModelPath, imagePath):
    clsModel = YOLO(clsModelPath)
    
    results = clsModel.predict(source=imagePath)
    
    if not results:
        print("No result from Torpedo Model")
        return False
    
    for result in results:
        if hasattr(result, 'probs'):
            top1_class_id = result.probs.top1
            top1_confidence = result.probs.top1conf
            
            # s = f"{top1_class_id} {result.names[top1_class_id]} {top1_confidence:.2f}"
            
            if result.names[top1_class_id] == "TorpedoFrame" and top1_confidence >= 0.99:
                return True
            
        else:
            print("Result dfoes not contain probability information")
    
    return False

