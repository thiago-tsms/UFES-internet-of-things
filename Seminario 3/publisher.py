import paho.mqtt.client as mqtt
import random
import time
import json


host = "mqtt.demo.konkerlabs.net"
topico = "data/ra7hji89lqd3/pub/001"


def run():
    while True:
        data = json.dumps({"temperature": random.randint(20,30), "unit": "celsius"})
        status = client.publish(topico, data)
        print(status)
        time.sleep(10)
    
    
if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('ra7hji89lqd3', '6s4ooUG7Rix1')
    client.connect(host, 1883)
    
    run()