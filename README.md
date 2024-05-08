<h1 align="center" id="title">Modular iot automation solution</h1>

<p align="center"><img src="https://socialify.git.ci/sansankarg/Modular-Automation-Server/image?name=1&amp;owner=1&amp;theme=Dark" alt="project-image"></p>

<p id="description">This project is a self-created server that is accessible globally serving as a foundational platform for various industrial or home automation endeavors. It allows users to update sensor details stream live videos with computer vision capabilities and customize recursive routines to meet specific needs. Importantly your project doesn't rely on paid third-party software or API providers making it particularly valuable for students and developers looking for a cost-effective and customizable solution for automation projects. With its versatility and accessibility this project empowers users to tailor automation systems according to their unique requirements fostering innovation and experimentation in the realm of automation technologies.</p>


## Requirements and its contributions

Here's how each requirement contributes to the overall functionality:

- **Hardware Requirements:**

Acquiring Raspberry Pi, Arduino boards with WiFi modules, sensors, and relays ensures you have the necessary physical components to build the automation system.
- **Local Server:**

Setting up a server on the Raspberry Pi enables local handling of web requests and responses. Global tunneling expands accessibility beyond the local network, allowing remote access and control.
- **Webpage Template:**
  
Customizing the provided webpage template tailors the user interface to suit the automation needs, providing an intuitive platform for interacting with the system.
- **Machine-to-Machine Messaging Protocol:**

Configuring an m2m protocol on the Raspberry Pi establishes a communication protocol between devices, sensors, and the server. This facilitates the seamless exchange of data and control commands.
- **Visual Communication with OpenCV:**

Integrating OpenCV brings advanced computer vision capabilities to the system, enabling tasks such as object detection, recognition, or tracking in industrial environments. This enhances the system's functionality and versatility.

- **Database:**

To store the sensor datas we need a database that runs in the server which is also integrated with the local server

- **Tunneling:**

Setting up a static server with ngrok ensures global accessibility to the local Flask server over the internet. This feature allows users to remotely monitor, manage, and control the automation system from anywhere.

By fulfilling these requirements, your automation project will offer a robust and flexible solution suitable for various industrial and home automation applications. Users will benefit from a user-friendly interface, efficient communication protocols, advanced computer vision capabilities, and remote accessibility, making it a valuable tool for automation enthusiasts and professionals alike.






## Installation

Before other installation, update the system

```bash
  sudo apt update && sudo apt upgrade
```
### Python installation
    
Install necessary package to download python

```bash
  sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

Download python

```bash
  wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
```
    
Extract and configure python

```bash
  tar -xvf Python-3.10.0.tar.xz
  cd Python-3.10.0
  ./configure --enable-optimizations
```
    
Build and install python

```bash
  make -j 4
  sudo make altinstall
```
    
Check whether python is installed

```bash
  python3.10 --version
```

### OpenCV installation
Please refer to this [link](https://pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) for installing OpenCV with the Patented "NonFree" algorithms. This installation process will be comprehensive and might take some time to complete

### Flask installation

To install flask

```bash
  sudo apt-get install python3-flask
```

### NGROK installation

Before installing ngrok you have to create a ngrok account for authtoken.After that

```bash
  wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
```

```bash
  sudo tar xvzf ./ngrok-v3-stable-linux-arm64.tgz -C /usr/local/bin
```


Now link with the ngrok account using aut token

```bash
  ngrok authtoken NGROK_AUTHTOKEN
```

### MQTT installation

Setting up an MQTT broker on a Raspberry Pi is a lengthy process. I don't want to take up too much space explaining it here, so I recommend following an excellent [tutorial](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/) for the installation. Feel free to pause this process, install it, and then return to continue.

Then to integrate mqtt with flask we need to install another package.

```bash
  pip install flask-mqtt
```

### SQLites installation

Step 1 − Go to SQLite download page, and download precompiled binaries from Windows section.

Step 2 − Download sqlite-shell-win32-*.zip and sqlite-dll-win32-*.zip zipped files.

Step 3 − Create a folder C:\>sqlite and unzip above two zipped files in this folder, which will give you sqlite3.def, sqlite3.dll and sqlite3.exe files.

Step 4 − Add C:\>sqlite in your PATH environment variable and finally go to the command prompt and issue sqlite3 command, which should display the following result.

```bash
SQLite version 3.45.2 2024-03-12 11:06:23 (UTF-16 console I/O)
Enter ".help" for usage hints.
Use ".open FILENAME" to reopen on a persistent database.
```




## Setting client for local updation

Here, I'm using NodeMCU for relay controls, and we can also update sensor data. To achieve this, we need to connect the NodeMCU to the MQTT broker for message exchange. To do so, upload the INO code to the NodeMCU. Before uploading, make sure to update your own WiFi and MQTT broker details in the code.

```cpp
const char *ssid = "XXXX";
const char *pass = "XXXX";

const char *mqtt_server = "192.168.XXX.XXX";
const int mqtt_port = 1883;
const char *mqttuser = "XXXX";
const char *mqttpass = "XXXX";

```
Make sure to add your SSID and password, as well as the IP address of your Raspberry Pi. If you've set a username and password to mqtt broker, update it accordingly, or leave it as null.
## To run the server

To run the server, we need to do three things:

### 1.Enable the MQTT broker

run this command to do that

```bash
  sudo systemctl start mosquitto
```


### 2.tunnel the local server to the internet through ngrok

For ephemeral domain

```bash
  ngrok http http://localhost:8080
```

For static domain

```bash
  ngrok http --domain=<YOUR-DOMAIN> 80
```

### 3.Run the Main.py

Finally, run the Flask server by executing.Make sure you are on the same directory of Server.

```bash
  python app.py
```

Open <YOUR-DOMAIN> in browser to view the server

## The Final Webpage

In this sample webpage template, we will have four pages: Control, View, Routine, and About.

- The Device page is for relay control, allowing us to control devices through our server globally.
  Function provided for relay control is : getstate()
 this will set relay control and return the status of relay.
- In the View page, we can view the live stream of video through the default Pi camera. Additionally, you can add sensor data for viewing.
  Function provided for this are : getdata() for sensor data, gen_frames() for video feed, getdirection()
 to move the camera
- The Routine page is highly customizable. I have uploaded three default routines with basic Python code, but you can easily customize them according to your industrial application needs.
  Function provided for routine is getroutine()
- Lastly, there is the About page where you can add your own details.

the all the funtions mentioned above are in functionsset.py file which get the value from the user and perform the output
the above mentioned pages screenshots were given below with basic functionalities.

Feel free to share your own implementations using this code for your application.

<h2>Project Screenshots:</h2>

<img src="https://github.com/sansankarg/Modular-Automation-Server/blob/master/Screenshots/image2.jpg" alt="project-screenshot" width="270" height="585">   <img src="https://github.com/sansankarg/Modular-Automation-Server/blob/master/Screenshots/image3.jpg" alt="project-screenshot" width="270" height="585">
<img src="https://github.com/sansankarg/Modular-Automation-Server/blob/master/Screenshots/image4.jpg" alt="project-screenshot" width="270" height="585">  <img src="https://github.com/sansankarg/Modular-Automation-Server/blob/master/Screenshots/image1.jpg" alt="project-screenshot" width="270" height="585">





