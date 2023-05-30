import paho.mqtt.client as mqtt
import json


host = "mqtt.prod.konkerlabs.net"
topico = "data/qidvpaonjdc2/sub/002"


def handler(client, userdata, msg):
    msg = msg.payload
    print(json.loads(msg))


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('qidvpaonjdc2', 'aYdnyhGOagkv')
    client.connect(host, 1883)
    client.subscribe(topico)
    client.on_message = handler
    client.loop_forever()
    