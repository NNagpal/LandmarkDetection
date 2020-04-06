# LandmarkDetection
This program marks the landmarks on the faces in image using OpenCV and dlib

## Requirement
**1.Landmark Detection model**
* Download the model using following link http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
* Extract the downloaded file

**2.Dclib**
* Download the dclib using following link https://sourceforge.net/projects/dclib/files/latest/download
* Extract the downloaded file
* Run the setup.py file present in the extracted folder

**3.Pytjon libarraies**
dlib, pandas, numpy, sys, dlib, cv2

## How to Run the LandmarkDetection programme
* model_path = path_to_the_model_dat_file
* image_path = path_to_the_imput_image
```bash
python run.py model_path image_path
```


## Output
1. Output.png : Image with all the facial landmarks marked on the image and the JawLine landmarks joined with a line
2. Output.csv : Coordinates of all the facial landmarks for all the faces present in the input image


## Running Example
python run.py 'src/model/' 'src/images/face1.jpeg'
