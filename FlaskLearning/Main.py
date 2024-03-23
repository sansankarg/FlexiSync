from flask import Flask, render_template, request, Response
import cv2
from flask_mqtt import Mqtt

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/view.html')
def view():
    print ("redirected to stream page")
    return render_template('view.html')

@app.route('/about.html')
def about():
    print ("redirected to stream page")
    return render_template('about.html')
@app.route('/home.html')
def home():
    print ("redirected to stream page")
    return render_template('home.html')
@app.route('/routine.html')
def routine():
    print ("redirected to stream page")
    return render_template('routine.html')

@app.route('/main_page.html')
def main():
    print ("redirected to main page")
    return render_template('main_page.html')

@app.route('/left')
def left():
    print ("Left")
    return ("nothing")

@app.route('/center')
def center():
    print ("Center")
    return ("nothing")

@app.route('/right')
def right():
    print ("Right")
    return ("nothing")

@app.route('/light_on')
def l_on():
    print ("Light is on")
    return ("nothing")


@app.route('/light_off')
def l_off():
    print ("Light is off")
    return ("nothing")

def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)