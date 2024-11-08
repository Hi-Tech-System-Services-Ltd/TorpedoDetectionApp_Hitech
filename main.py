import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *
from app.cam import cam1, cam2, cam3  # Import specific functions from consolidated cam.py
from components.findLatestImageName import *
from database.pushData import *

# Constants
TORPEDO_ID = 55  # TODO: replace with OCR/number detection
IMAGES_DIRS = {
    1: "images_cam1",
    2: "images_cam2",
    3: "images_cam3"
}

def process_camera(cam_id, cam_func):
    """
    Generic camera processing function that handles detection and data pushing for any camera
    
    Args:
        cam_id (int): Camera identifier (1, 2, or 3)
        cam_func (callable): Camera function to call (cam1, cam2, or cam3)
    """
    try:
        result = cam_func()
        
        if result is None:
            print(f"Cam{cam_id}: No Detection or an error occurred.")
            return
            
        c_x, c_y, w, h = result
        if c_x == -99:  # Check for no detection case
            print(f"Cam{cam_id}: No Detection.")
            return
            
        filename = findLatestImageName(IMAGES_DIRS[cam_id])
        pushData_API(TORPEDO_ID, c_x, c_y, w, h, cam_id, filename)
        print(f"Cam{cam_id}-data_pushed")
        
    except Exception as e:
        print(f"Error processing camera {cam_id}: {e}")

def cam1_thread_func():
    """Thread function for Camera 1 processing"""
    process_camera(1, cam1)

def cam2_thread_func():
    """Thread function for Camera 2 processing"""
    process_camera(2, cam2)

def cam3_thread_func():
    """Thread function for Camera 3 processing"""
    process_camera(3, cam3)

def main():
    """
    Main function that manages camera processing threads.
    Creates and manages threads for each camera, running them in parallel.
    """
    try:
        while True:
            # Create threads
            threads = [
                threading.Thread(target=cam1_thread_func, daemon=True),
                threading.Thread(target=cam2_thread_func, daemon=True),
                # Uncomment below line to enable camera 3
                # threading.Thread(target=cam3_thread_func, daemon=True),
            ]
            
            # Start all threads
            for thread in threads:
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            # Clean up memory
            gc.collect()
            
            # Wait before next iteration
            time.sleep(1)

    except Exception as e:
        print(f"Main thread exception: {e}")
        raise  # Re-raise the exception for proper error handling

if __name__ == "__main__":
    main()