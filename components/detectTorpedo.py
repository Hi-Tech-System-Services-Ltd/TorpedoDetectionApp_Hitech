import sys
import os
import logging
from typing import Tuple
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def detectTorpedo(detectModelPath: str, imagePath: str) -> Tuple[int, int, int, int]:
    """
    Detect torpedoes in an image using a YOLO model and return the coordinates of the bounding box.

    Parameters:
    detectModelPath (str): Path to the YOLO model.
    imagePath (str): Path to the image to be processed.

    Returns:
    tuple: Coordinates of the bounding box (x1, y1, x2, y2) or (-99, -99, -99, -99) if no box is found.
    """
    try:
        detectModel = YOLO(detectModelPath)
    except Exception as e:
        logging.error(f"Error loading model: {e}")
        return -99, -99, -99, -99
    
    try:
        results = detectModel(imagePath)
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return -99, -99, -99, -99
    
    if not results:
        logging.info("No bounding box")
        return -99, -99, -99, -99
    
    for result in results:
        boxes = result.boxes
        if not boxes:
            logging.info("No boxes found")
            return -99, -99, -99, -99
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().detach().numpy().astype(int)
            return x1, y1, x2, y2
    
    return -99, -99, -99, -99