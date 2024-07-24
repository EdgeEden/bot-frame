import paho.mqtt.client as mqtt
import os
import time

mqtt_host = "47.109.75.121"
mqtt_port = 1883
client_id = "lzb_will"
topicsub = "/lzb_espWill"
pipe_path = '/tmp/pipe_demo' 


def connect_mqtt():
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(mqtt_host, mqtt_port)
    return client


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}\n")


def on_message(client, userdata, message):
    print(f"Received `{message.payload.decode()}` from `{message.topic}` topic")
    if message.payload.decode() == "espDown":
        print("espDown")
        with open(pipe_path, 'w') as f:
            f.write("群【南12-615】【will】 发送了：espDown")

def subscribe(client):
    client.subscribe(topicsub)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    while True:
        time.sleep(20)
        pass


run()
