#include <ESP8266WiFi.h>
#include<PubSubClient.h>

const char *ssid = "Arthur";
const char *pass = "kzut8x4c";

const char *mqtt_server = "192.168.66.51";
const int mqtt_port = 1883;
const char *mqttuser = "arthur";
const char *mqttpass = "5464";

const int pin1 = D1;
const int pin2 = D2;
const int pin3 = D5;
const int pin4 = D6;

void callback(String topic,byte* payload,unsigned int length1){
  Serial.print("Got the msg");
  String msgg;

  for(int i=0;i<length1;i++){
      Serial.print((char)payload[i]);
      msgg += (char)payload[i];
  }
  if(topic == "connect")
    {
    if(msgg == "1_onn"){
      digitalWrite(pin1,HIGH);
      Serial.print("\n up \n ");
    }
    else if(msgg == "1_off")
    {
      digitalWrite(pin1,LOW);
      Serial.print("\n down");
    }
    else if(msgg == "2_onn"){
      digitalWrite(pin2,HIGH);
      Serial.print("\n up \n ");
    }
    else if(msgg == "2_off")
    {
      digitalWrite(pin2,LOW);
      Serial.print("\n down");
    }
    else if(msgg == "3_onn"){
      digitalWrite(pin3,HIGH);
      Serial.print("\n up \n ");
    }
    else if(msgg == "3_off")
    {
      digitalWrite(pin3,LOW);
      Serial.print("\n down");
    }
    else if(msgg == "4_onn"){
      digitalWrite(pin4,HIGH);
      Serial.print("\n up \n ");
    }
    else if(msgg == "4_off")
    {
      digitalWrite(pin4,LOW);
      Serial.print("\n down");
    }
  }
}
WiFiClient espclient;
PubSubClient client(mqtt_server,1883,callback,espclient);
void setup() {
  Serial.begin(115200);
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);
  pinMode(pin4,OUTPUT);
  WiFi.begin(ssid, pass);
  Serial.println("Connecting WiFi..")
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print("..");
  }
  Serial.println("Connected to wifi");
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void reconnect(){
  while (!client.connected()) {
    Serial.println("Connecting MQTT..");
    if (client.connect("ESP8266Client", mqttuser, mqttpass )) {
      Serial.println("Connected to MQTT");
      client.subscribe("connect");
    } else {
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void loop()
{
  if(!client.connected()){
    reconnect();
  }
  client.loop();
}