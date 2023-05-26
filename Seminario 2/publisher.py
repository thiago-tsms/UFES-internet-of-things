import sys
import paho.mqtt.client as mqtt
import random
import time


host = "localhost"
topico = "sd/iot"

msg_tamanho = int(sys.argv[1])
frequencia_envio = int(sys.argv[2])

msg = "".join(['a' for _ in range(msg_tamanho)])


def run():
    while True:
        client.publish(topico, msg)
        time.sleep(1/frequencia_envio)
    
    
if __name__ == '__main__':
    client = mqtt.Client(f'publisher-{random.random()}')
    client.connect(host)
    
    run()