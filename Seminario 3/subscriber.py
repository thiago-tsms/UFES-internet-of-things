import paho.mqtt.client as mqtt
import json


host = "mqtt.prod.konkerlabs.net"
port = 1883

dispositivo_konker_user = "dd8q0k9hr7lg"
dispositivo_konker_password = "Tbo0ge6lDAPU"

channel_temperatura_simulada = "01"
channel_temperatura_lida = "02"
channel_pressao_lida = "03"

topico_temperatura_simulada = f"data/{dispositivo_konker_user}/sub/{channel_temperatura_simulada}"
topico_temperatura_lida = f"data/{dispositivo_konker_user}/sub/{channel_temperatura_lida}"
topico_pressao_lida = f"data/{dispositivo_konker_user}/sub/{channel_pressao_lida}"


def handler(client, userdata, msg):
    data = msg.payload
    print('------------------------------')
    print(f'Origem: {msg.topic}')
    print(json.loads(data))
    print('------------------------------\n')


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set(dispositivo_konker_user, dispositivo_konker_password)
    client.connect(host, 1883)
    
    client.subscribe(topico_temperatura_simulada)
    client.subscribe(topico_temperatura_lida)
    client.subscribe(topico_pressao_lida)
    
    client.on_message = handler
    client.loop_forever()
    