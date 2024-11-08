

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('TorpedoDetectionApp_Hitech')))


from app.cam1 import *
from app.cam2 import *
from app.cam3 import *
from app.digitalCam import *
from app.directionOfMotion import *
from app.ocr import *

from components.calculateBBoxInfo import *
from components.clsTorpedo import *
from components.deleteFiles import *
from components.detectTorpedo import *
from components.findLatestImageName import *
from components.findLatestImagePath import *
from components.makeCopy import *
from components.saveImage import *

from imports import * 
from main import *
from wrapperScript import *


# print("Current working directory:", os.getcwd())
# print("Python path:", sys.path)

print("All imports are in path and is working")
