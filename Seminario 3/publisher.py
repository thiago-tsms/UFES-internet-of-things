import paho.mqtt.client as mqtt
import random
import time
import json


host = "mqtt.prod.konkerlabs.net"
port = 1883

dispositivo_konker_user = "21j96ala4du1"
dispositivo_konker_password = "gb72Ij9faXMw"

channel = "01"
topico = f"data/{dispositivo_konker_user}/pub/{channel}"


def run():
    while True:
        data = json.dumps({"temp": random.randint(20,30), "unit": "celsius"})
        status = client.publish(topico, data)
        print(status)
        time.sleep(10)
    
    
if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set(dispositivo_konker_user, dispositivo_konker_password)
    client.connect(host, port)
    
    run()