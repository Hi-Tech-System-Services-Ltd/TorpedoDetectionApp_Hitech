
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


stream_images_cam3 = "E:/flir/images/thermal_image_3.jpg"
# stream_images_cam3 = 'E:\\flir\\TorpedoDetectionApp_Hitech\\testing_images\\cam3.jpg'
images_cam3 = "E:/flir/TorpedoDetectionApp_Hitech/images_cam3"
temp_cam3 = "E:/flir/TorpedoDetectionApp_Hitech/temp_cam3"

cls_model_path_cam3 = "E:/flir/TorpedoDetectionApp_Hitech/models/cam3_classify.pt"
detect_model_path_cam3 = "E:/flir/TorpedoDetectionApp_Hitech/models/cam3_detect.pt"

temp_filename = f"temp_cam3.jpg"
final_filename = f"cam3_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

images = "E:/flir/TorpedoDetectionApp_Hitech/images"

def cam3():
    deleteFiles(temp_cam3)
    makeCopy(stream_images_cam3, temp_cam3, temp_filename)
    temp_image_cam3 = findLatestImagePath(temp_cam3)
    torpedoInframe = clsTorpedo(cls_model_path_cam3, temp_image_cam3)
    
    if not torpedoInframe:
        return -99, -99, -99, -99
    
    result = detectTorpedo(detect_model_path_cam3, temp_image_cam3)
    if result is None or result == (-99, -99, -99, -99):
        return -99, -99, -99, -99
    

    x1, y1, x2, y2 = result
    saveImage(temp_image_cam3, images_cam3, final_filename)
    saveImage(temp_image_cam3, images, final_filename)
    c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
    return c_x, c_y, w, h
