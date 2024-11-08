
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


stream_images_cam2 = "E:\\flir\\images\\thermal_image_2.jpg"
images_cam2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\images_cam2"
temp_cam2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\temp_cam2"

cls_model_path_cam2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam2_classify.pt"
detect_model_path_cam2 = "E:\\flir\\TorpedoDetectionApp_Hitech\\models\\cam2_detect.pt"

temp_filename = f"temp_cam2.jpg"
final_filename = f"cam2_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

images = "E:\\flir\\TorpedoDetectionApp_Hitech\\images"

def cam2():
    deleteFiles(temp_cam2)
    makeCopy(stream_images_cam2, temp_cam2, temp_filename)
    temp_image_cam2 = findLatestImagePath(temp_cam2)
    torpedoInframe = clsTorpedo(cls_model_path_cam2, temp_image_cam2)
    
    if torpedoInframe:
        x1, y1, x2, y2 = detectTorpedo(detect_model_path_cam2, temp_cam2)
        
        if x1 == None:
            print("Detect Torpedo Returned None")
            return -99, -99, -99, -99
        else:
            saveImage(temp_image_cam2, images_cam2, final_filename)
            saveImage(temp_image_cam2, images, final_filename)
            c_x, c_y, w, h = calculateBBoxInfo(x1, y1, x2, y2)
            return c_x, c_y, w, h
    