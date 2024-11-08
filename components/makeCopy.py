import sys
import os
import shutil
import logging
from typing import Optional
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def makeCopy(src: str, dst_path: str, filename: str) -> Optional[str]:
    """
    Copy a file from the source path to the destination directory with the specified filename.

    Parameters:
    src (str): Source file path.
    dst_path (str): Destination directory path.
    filename (str): Name of the file in the destination directory.

    Returns:
    Optional[str]: The destination path of the copied file or None if an error occurred.
    """
    try:
        dst = os.path.join(dst_path, filename)
        shutil.copy2(src, dst)
        logging.info(f"Image saved to {dst}")
        return dst
    except Exception as e:
        logging.error(f"Error: {e}")
        return None