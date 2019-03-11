from firebase import firebase
import time 
import imutils
import numpy as np 
import imutils 
import cv2

camera = cv2.VideoCapture(0)
firebase_link = "https://watchout-466b3.firebaseio.com/"
firebase = firebase.FirebaseApplication(firebase_link   )
import datetime
time_d = datetime.datetime.now().time()
time_d = str(time_d)

def getLocation():
    lat = "30" #dummy
    lon = "49"#dummy
    location = {
        "lat": lat,
        "long": lon
    }
    return location

def firebase_push():

    location = getLocation()
    data = {
        'time': time_d,
        'location': location,

    }
    result = firebase.patch(firebase_link+"/latest_data", data)


# detected = 0
# if(detected==0){

# }
# time.sleep(5)

detected =1 
if(detected ==1):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
    capture_duration=10
    firebase_push()
    
    start_time = time.time()
    while( int(time.time()) - int(start_time) < capture_duration ):
        
        ret, frame = camera.read()
        if ret==True:
            # frame = cv2.flip(frame,0)
            out.write(frame)
            cv2.imshow('frame',frame)
        else:
            break

    camera.release()
    out.release()
