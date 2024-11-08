import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

def calculateBBoxInfo(x1: int, y1: int, x2: int, y2: int) -> tuple:
    """
    Calculate the center coordinates, width, and height of a bounding box.

    Parameters:
    x1 (int): Top-left x-coordinate
    y1 (int): Top-left y-coordinate
    x2 (int): Bottom-right x-coordinate
    y2 (int): Bottom-right y-coordinate

    Returns:
    tuple: (center_x, center_y, width, height)
    """
    if x2 <= x1 or y2 <= y1:
        raise ValueError("Invalid coordinates: x2 should be greater than x1 and y2 should be greater than y1.")
    
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    
    width = x2 - x1
    height = y2 - y1
    
    return center_x, center_y, width, height