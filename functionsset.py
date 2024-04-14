from flask import Flask, render_template, request, Response
import os
import cv2
#from main import mqtt
class functions():
    def setdata(self, value):
        self.getdirection('pos')
        print("redirected to view page")
        return render_template('access.html', data = value)
    def getdirection(id):
        if request.method == 'POST':
            id = request.form.get(id)
            if id == 'Left':
                print("Left")
                os.system("python ser.py 1 2 0.1 1")
            elif id == "Center":
                print("Center")
                os.system("python ser.py 89 90 0.3 1")
            elif id == "Right":
                print("Right")
                os.system("python ser.py 179 180 0.1 1")

    def getstate(id, mqttmsgon, mqttmsgoff):
        if request.method == 'POST':
            id = request.form.get(id)
            if id == 'On':
                # mqtt.publish('connect', mqttmsgoff)
                print(mqttmsgon, " published as a mqtt message")
            else:
                # mqtt.publish('connect', mqttmsgon)
                print(mqttmsgoff, " published as a mqtt message")

    def getroutine(id, filename):
        if request.method == 'POST':
            id = request.form.get(id)
            if id == 'enable':
                # print ("Routine 3 is enabled")
                str = "python " + filename
                os.system(str)

    def gen_frames(self):
        camera = cv2.VideoCapture(0)
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#
# def getdirection(id):
#     if request.method == 'POST':
#         id = request.form.get(id)
#         if id == 'Left':
#             print("Left")
#             os.system("python ser.py 1 2 0.1 1")
#         elif id == "Center":
#             print("Center")
#             os.system("python ser.py 89 90 0.3 1")
#         elif id == "Right":
#             print("Right")
#             os.system("python ser.py 179 180 0.1 1")
#
# def getstate(id, mqttmsgon, mqttmsgoff):
#     if request.method == 'POST':
#         id = request.form.get(id)
#         if id == 'On':
#             # mqtt.publish('connect', mqttmsgoff)
#             print(mqttmsgon," published as a mqtt message")
#         else:
#             # mqtt.publish('connect', mqttmsgon)
#             print(mqttmsgoff," published as a mqtt message")
#
# def getroutine(id, filename):
#     if request.method == 'POST':
#         id = request.form.get(id)
#         if id == 'enable':
#             #print ("Routine 3 is enabled")
#             str = "python "+filename
#             os.system(str)