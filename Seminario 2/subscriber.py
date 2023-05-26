import sys
import paho.mqtt.client as mqtt
import random


host = "localhost"
topico = "sd/iot"
url = "./res/recebidos.txt"
noSave = 1


def handler(client, userdata, msg):
    msg = msg.payload
    
    if sys.argv[2]:
        noSave = int(sys.argv[2])
        
    if noSave == 1:
        with open(url, 'a') as arquivo:
            arquivo.write(f'\n{len(msg)}')
        arquivo.close()


def run():
    while True:
        None
    
    
if __name__ == '__main__':
    ur = sys.argv[1]
    if ur:
        url = ur
    
    client = mqtt.Client(f'subscriber-{random.random()}')
    client.connect(host)
    client.subscribe(topico)
    client.on_message = handler
    client.loop_start()
    
    run()