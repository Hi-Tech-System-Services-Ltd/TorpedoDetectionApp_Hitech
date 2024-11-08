import sys
import os
import logging
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

def deleteFiles(dir_path: str) -> None:
    """
    Delete all files in the specified directory.

    Parameters:
    dir_path (str): Path to the directory from which files will be deleted.

    Returns:
    None
    """
    try:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            for file_name in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file_name)
                
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    logging.info(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    logging.info(f"Skipping directory: {file_path}")
                
            logging.info("All files in the directory have been deleted.")
            
        else:
            logging.error("Invalid directory path")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")