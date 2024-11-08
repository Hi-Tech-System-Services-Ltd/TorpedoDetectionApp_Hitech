import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

# Import required components
from components.calculateBBoxInfo import *
from components.clsTorpedo import *
from components.deleteFiles import *
from components.detectTorpedo import *
from components.findLatestImageName import *
from components.findLatestImagePath import *
from components.makeCopy import *
from components.saveImage import *

# Camera 1 Configuration
STREAM_IMAGES_CAM1 = "E:\\flir\\images\\thermal_image_1.jpg"
IMAGES_CAM1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\images_cam1"
TEMP_CAM1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\temp_cam1"
CLS_MODEL_PATH_CAM1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam1_classify.pt"
DETECT_MODEL_PATH_CAM1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam1_detect.pt"

# Camera 2 Configuration
STREAM_IMAGES_CAM2 = "E:\\flir\\images\\thermal_image_2.jpg"
IMAGES_CAM2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\images_cam2"
TEMP_CAM2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\temp_cam2"
CLS_MODEL_PATH_CAM2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam2_classify.pt"
DETECT_MODEL_PATH_CAM2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam2_detect.pt"

# Camera 3 Configuration
STREAM_IMAGES_CAM3 = "E:\\flir\\images\\thermal_image_3.jpg"
IMAGES_CAM3 = "E:\\flir\\TorpedoDetectionApp_Hitech\\images_cam3"
TEMP_CAM3 = "E:\\flir\\TorpedoDetectionApp_Hitech\\temp_cam3"
CLS_MODEL_PATH_CAM3 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam3_classify.pt"
DETECT_MODEL_PATH_CAM3 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam3_detect.pt"

# Common Configuration
IMAGES_DIR = "E:\\flir\\TorpedoDetectionApp_Hitech\\images"

def process_camera(cam_number, stream_path, temp_dir, images_dir, cls_model_path, detect_model_path):
    """
    Generic camera processing function that handles torpedo detection for any camera
    
    Args:
        cam_number (int): Camera identifier (1, 2, or 3)
        stream_path (str): Path to the thermal image stream
        temp_dir (str): Directory for temporary files
        images_dir (str): Directory to save detected images
        cls_model_path (str): Path to classification model
        detect_model_path (str): Path to detection model
    
    Returns:
        tuple: (center_x, center_y, width, height) of detected torpedo or (-99, -99, -99, -99) if not detected
    """
    # Generate filenames
    temp_filename = f"temp_cam{cam_number}.jpg"
    final_filename = f"cam{cam_number}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
    
    # Clean temporary directory
    deleteFiles(temp_dir)
    
    # Copy stream image to temp directory
    makeCopy(stream_path, temp_dir, temp_filename)
    temp_image = findLatestImageName(temp_dir)
    
    # Check if torpedo is in frame using classification model
    torpedoInframe = clsTorpedo(cls_model_path, temp_image)
    
    if torpedoInframe:
        # Detect torpedo location using detection model
        x1, y1, x2, y2 = detectTorpedo(detect_model_path, temp_dir)
        
        if x1 is None:
            print(f"Detect Torpedo Returned None for Camera {cam_number}")
            return -99, -99, -99, -99
        else:
            # Save the image with detection
            saveImage(temp_image, images_dir, final_filename)
            saveImage(temp_image, IMAGES_DIR, final_filename)
            
            # Calculate bounding box information
            c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
            return c_x, c_y, w, h
    
    return -99, -99, -99, -99

def cam1():
    """
    Process Camera 1 feed for torpedo detection
    
    Returns:
        tuple: (center_x, center_y, width, height) of detected torpedo or (-99, -99, -99, -99) if not detected
    """
    return process_camera(1, STREAM_IMAGES_CAM1, TEMP_CAM1, IMAGES_CAM1, 
                         CLS_MODEL_PATH_CAM1, DETECT_MODEL_PATH_CAM1)

def cam2():
    """
    Process Camera 2 feed for torpedo detection
    
    Returns:
        tuple: (center_x, center_y, width, height) of detected torpedo or (-99, -99, -99, -99) if not detected
    """
    return process_camera(2, STREAM_IMAGES_CAM2, TEMP_CAM2, IMAGES_CAM2,
                         CLS_MODEL_PATH_CAM2, DETECT_MODEL_PATH_CAM2)

def cam3():
    """
    Process Camera 3 feed for torpedo detection
    
    Returns:
        tuple: (center_x, center_y, width, height) of detected torpedo or (-99, -99, -99, -99) if not detected
    """
    return process_camera(3, STREAM_IMAGES_CAM3, TEMP_CAM3, IMAGES_CAM3,
                         CLS_MODEL_PATH_CAM3, DETECT_MODEL_PATH_CAM3)