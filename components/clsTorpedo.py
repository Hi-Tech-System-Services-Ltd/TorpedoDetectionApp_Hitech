import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from typing import Union

def clsTorpedo(clsModelPath: str, imagePath: str) -> Union[bool, None]:
    """
    Classify an image using a YOLO model to detect 'TorpedoFrame'.

    Parameters:
    clsModelPath (str): Path to the YOLO model.
    imagePath (str): Path to the image to be classified.

    Returns:
    bool: True if 'TorpedoFrame' is detected with 0.99 confidence, False otherwise.
    """
    try:
        clsModel = YOLO(clsModelPath)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
    
    try:
        results = clsModel.predict(source=imagePath)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
    
    if not results:
        print("No result from Torpedo Model")
        return False
    
    for result in results:
        if hasattr(result, 'probs'):
            top1_class_id = result.probs.top1
            top1_confidence = result.probs.top1conf
            
            if result.names[top1_class_id] == "TorpedoFrame" and top1_confidence == 0.99:
                return True
        else:
            print("Result does not contain probability information")
    
    return False
