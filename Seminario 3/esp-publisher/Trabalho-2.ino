/*
  broker: mqtt.prod.konkerlabs.net
  porta: 1883

  topicoSensTemp: data/<usuario do dispositivo>/pub/<canal (01)>
  topicoSensPress: data/<usuario do dispositivo>/pub/<canal (02)>
  mensagem:
    temp - temperatura
    press - preção

*/

#include "ESP8266TimerInterrupt.h"
#include <Wire.h>
#include <Adafruit_BMP280.h>

#include <ArduinoMqttClient.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#include <ArduinoJson.h>

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

ESP8266Timer ITimer;
Adafruit_BMP280  bmp280;

StaticJsonDocument<200> docTemp, docPress;

const char *ssid = "PATOLINO";
const char *pass = "patolino2021";

const char *broker = "mqtt.prod.konkerlabs.net";
const char *broker_user = "9jbnm4pcgqbn";
const char *broker_pass = "bRbtp0EtHDFT";
const int port = 1883;
const char *topicoSensTemp  = "data/9jbnm4pcgqbn/pub/01";
const char *topicoSensPress  = "data/9jbnm4pcgqbn/pub/02";

bool flag = false;

#define LED 2
#define BMP280_I2C_ADDRESS  0x76

void onMessage(int mSize);
void config_i2c();

void ICACHE_RAM_ATTR TimerHandler(void){
  flag = true;
}

void setup() {
  Serial.println("Iniciando");
  Serial.begin(74880);
  pinMode(LED, OUTPUT);

  config_i2c();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  mqttClient.setUsernamePassword(broker_user, broker_pass);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  ITimer.attachInterruptInterval(5000000, TimerHandler);
}

void loop() {
  mqttClient.poll();

  if(flag){
    String msg1 ,msg2;

    docTemp["temp"] = bmp280.readTemperature();
    docTemp["unit"] = "celsius";
    serializeJson(docTemp, msg1);
    Serial.println(msg1);
    mqttClient.beginMessage(topicoSensTemp);
    mqttClient.print(msg1);
    mqttClient.endMessage();

    docPress["press"] = bmp280.readPressure();
    docTemp["unit"] = "pascal";
    serializeJson(docPress, msg2);
    Serial.println(msg2);
    mqttClient.beginMessage(topicoSensPress);
    mqttClient.print(msg2);
    mqttClient.endMessage();

    flag = false;
  }
}

void config_i2c(){
  Wire.begin();  // set I2C pins [SDA = D2, SCL = D1], default clock is 100kHz
  if(bmp280.begin(BMP280_I2C_ADDRESS) == 0) {
    Serial.println("Nao conseguiu reconhecer o Sensor");
    while(1);
  }
  Serial.println("I2C Iniciado");
}

/*void onMessage(int mSize){
  String msg = "";

  while (mqttClient.available()) msg += (char)mqttClient.read();
  Serial.println(msg);

  if(msg.equals("ON")) digitalWrite(LED, false);
  else if(msg.equals("OFF")) digitalWrite(LED, true);
}*/