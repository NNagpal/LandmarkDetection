import cv2
import numpy as np
import dlib
import pandas as pd
import sys

model_path = sys.argv[1]
image_path = sys.argv[2]


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path+"shape_predictor_68_face_landmarks.dat")
frame = cv2.imread(image_path)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = detector(gray)
face_count = 1
output = pd.DataFrame(columns = ['face_number','face_bbox','landmark_pos','x','y'])
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
   

    landmarks = predictor(gray, face)
    coordinates_x = []
    coordinates_y = []
    landmark_pos = []
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        coordinates_x.extend([x])
        coordinates_y.extend([y])
        landmark_pos.extend([n])
        if((n>0) & (n<17)):
            cv2.line(frame, (x, y), (x_prev, y_prev), (0, 255, 0), thickness=1, lineType=8)
            x_prev = x
            y_prev = y
        else:
            cv2.circle(frame, (x, y), 1, (255, 0, 0), -1)
            x_prev = x
            y_prev = y
    
    output = pd.concat([output,pd.DataFrame({'face_number':'face_'+str(face_count),'face_bbox':str(face),'landmark_pos':landmark_pos,'x':coordinates_x,'y':coordinates_x})])
    face_count = face_count+1

output.to_csv('Output.csv')
cv2.imwrite('Output.png',frame)
