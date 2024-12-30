# TorpedoDetectionApp_Hitech

---

## Features

- **Object Detection and Classification**: Utilizes pre-trained deep learning models to identify and classify torpedoes from camera feeds.
- **Multi-Camera Support**: Supports detection across multiple camera inputs.
- **Modular Design**: Ensures the application can be extended and maintained easily.
- **Testing Framework**: Includes unit tests to validate core functionalities
---

## Folder Structure

```
TorpedoDetectionApp_Hitech
|-.venv                # Virtual environment for the project
├── app                # Contains individual camera functions
│   ├── cam1.py
│   ├── cam2.py
│   ├── cam3.py
├── components         # Contains core functions for the project
│   ├── calculateBBoxInfo.py
│   ├── clsTorpedo.py
│   ├── deleteFiles.py
│   ├── detectTorpedo.py
│   ├── findLatestImageName.py
│   ├── findLatestImagePath.py
│   ├── makeCopy.py
│   └── saveImage.py
├── database           # Handles database connectivity
│   └── pushData.py
├── models             # Contains deep learning models
│   ├── cam1_classify.pt
│   ├── cam2_classify.pt
│   ├── cam3_classify.pt
│   ├── cam1_detect.pt
│   ├── cam2_detect.pt
│   └── cam3_detect.pt
├── imports.py         # Centralized imports for the project
├── main.py            # Main function to run the application
├── test               # Unit tests for core functionalities
│   ├── test_calculateBBoxInfo.py
│   ├── test_cam.py
│   ├── test_clsTorpedo.py
│   ├── test_deleteFiles.py
│   ├── test_detectModel.py
│   ├── test_detectTorpedo.py
│   ├── test_digitalCam.py
│   ├── test_env.py
│   ├── test_findLatestImageName.py
│   ├── test_findLatestImagePath.py
│   └── test_imports.py
├── images             # Directory for saving analysis images
├── images_cam1    # Images from cam1
├── images_cam2    # Images from cam2
├── images_cam3    # Images from cam3
├── temp_cam1      # Temporary storage for cam1 stream
├── temp_cam2      # Temporary storage for cam2 stream
├── temp_cam3      # Temporary storage for cam3 stream
├── testing_images # Images used for testing
|-.env                 # Environment variables
|-requirements.txt     # Dependencies for the project
```

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Hi-Tech-System-Services-Ltd/TorpedoDetectionApp_Hitech.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TorpedoDetectionApp_Hitech
   ```

3. Create and activate a virtual environment:
   - **Linux/macOS**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Project

1. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate  # For Windows
   source .venv/bin/activate  # For Linux/macOS
   ```

2. Run the application:
   ```bash
   python main.py
   ```
   The application will execute in an infinite loop as a system process.

---


## License

This project is a property of Hi-Tech System Services Limited. All rights reserved.

---

