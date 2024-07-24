import paho.mqtt.client as mqtt
import time

mqtt_host = "47.109.75.121"
mqtt_port = 1883
client_id = "lzb_test"
topicpub = "/lzb_command"
topicsub = "/lzb_report"
isalive = False

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
    global isalive
    if message.payload.decode() == "11":
        isalive = True

def publish(client):
    msg = f"1"
    result = client.publish(topicpub, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topicpub}`")
    else:
        print(f"Failed to send message to topic {topicpub}")

def subscribe(client):
    client.subscribe(topicsub)
    client.on_message = on_message

def run():
    global isalive
    isalive = False
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    publish(client)
    time.sleep(2)
    if isalive:
        print("Device is alive")
        client.loop_stop()
        return True
    else:
        print("Device is dead")
        client.loop_stop()
        return False



