
from flask import Flask, Response
import cv2
import numpy as np

app = Flask(__name__)
cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

def stream():
    while True:
        ret,frame = cap.read()

        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg',frame)

        if not ret:
            break

        frame_bytes = buffer.tobytes()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')
        
@app.route('/')
def video_feed():
    return Response(stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':

    app.run(host='0.0.0.0',port=5000, debug=False)

        
