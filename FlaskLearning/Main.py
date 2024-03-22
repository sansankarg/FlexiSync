from flask import Flask, render_template, request, Response
import cv2

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/videostream.html')
def vidStr():
    print ("redirected to stream page")
    return render_template('videostream.html')

@app.route('/main_page.html')
def main():
    print ("redirected to main page")
    return render_template('main_page.html')

@app.route('/controls.html')
def controls():
    print ("redirected to control page")
    return render_template('controls.html')

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


camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)