import sys
import os
import glob
import logging
from typing import Optional
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def findLatestImageName(dir_path: str) -> Optional[str]:
    """
    Find the latest image file in the specified directory based on the last access time.

    Parameters:
    dir_path (str): Path to the directory to search for image files.

    Returns:
    Optional[str]: The name of the latest image file or None if no images are found.
    """
    image_extensions = ('*.jpg', '*.jpeg', '*.png')  
    image_files = []
    
    try:
        for ext in image_extensions:
            image_files.extend(glob.glob(os.path.join(dir_path, ext)))
        
        if not image_files:
            logging.info("No images found in the directory")
            return None
        
        latest_image = max(image_files, key=os.path.getatime)
        return os.path.basename(latest_image)
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None