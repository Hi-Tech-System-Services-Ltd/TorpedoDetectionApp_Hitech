
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))

from imports import *

from components.calculateBBoxInfo import *
from components.clsTorpedo import *
from components.deleteFiles import *
from components.detectTorpedo import *
from components.clsTorpedo import *
from components.findLatestImageName import *
from components.findLatestImagePath import *
from components.makeCopy import *
from components.saveImage import *


stream_images_cam1 = "E:\\flir\\images\\thermal_image_1.jpg"
# stream_images_cam1 = 'E:\\flir\\TorpedoDetectionApp_Hitech\\testing_images\\cam1.jpg'
images_cam1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\images_cam1"
temp_cam1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\temp_cam1"

cls_model_path_cam1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam1_classify.pt"
detect_model_path_cam1 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam1_detect.pt"

temp_filename = f"temp_cam1.jpg"
final_filename = f"cam1_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

images = "E:\\flir\\TorpedoDetectionApp_Hitech\\images"

def cam1():
    deleteFiles(temp_cam1)
    makeCopy(stream_images_cam1, temp_cam1, temp_filename)
    temp_image_cam1 = findLatestImagePath(temp_cam1)
    torpedoInframe = clsTorpedo(cls_model_path_cam1, temp_image_cam1)
    
    if not torpedoInframe:
        return -99, -99, -99, -99
    
    result = detectTorpedo(detect_model_path_cam1, temp_image_cam1)
    if result is None or result == (-99, -99, -99, -99):
        return -99, -99, -99, -99
    
    x1, y1, x2, y2 = result
    saveImage(temp_image_cam1, images_cam1, final_filename)
    saveImage(temp_image_cam1, images, final_filename)
    c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
    return c_x, c_y, w, h
