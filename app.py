from flask import Flask, render_template, Response, request
from functionsset import functions as fn
from flask_mqtt import Mqtt
from calldatabase import data1, data2, data3

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 1883  #default one No need to change
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = '' #Fill both username and password if you have one or else leave it empty
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

# mqtt = Mqtt(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('about.html')

@app.route('/control.html', methods=['GET', 'POST'])
def control():
    fn.getstate('dev1', "1_onn", "1_off")
    fn.getstate('dev2', "2_onn", "2_off")
    fn.getstate('dev3', "3_onn", "3_off")
    fn.getstate('dev4', "4_onn", "4_off")
    print("redirected to controls page")
    return render_template('control.html')

@app.route('/access.html', methods=['GET', 'POST'])
def access():
    value = {'1': fn.getdata(fn, 's1'), '2': fn.getdata(fn, 's2'), '3': fn.getdata(fn, 's3')}
    print ("redirected to view page")
    return render_template('access.html', data = value)

@app.route('/automation.html', methods = ['GET', 'POST'])
def automation():
    fn.getroutine('routine1', "routine1.py")
    fn.getroutine('routine2', "routine2.py")
    fn.getroutine('routine3', "routine3.py")
    print ("redirected to routine page")
    return render_template('automation.html')

@app.route('/about.html')
def about():
    print ("redirected to about page")
    return render_template('about.html')

@app.route('/video_feed')
def video_feed():
    return Response(fn.gen_frames(fn), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)