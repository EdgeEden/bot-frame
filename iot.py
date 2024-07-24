import json
import time
import paho.mqtt.client as mqtt

# set the device info, include product key, device name, and device secret
productKey = "k0y1pp87qA5"
deviceName = "ECSdemo"
deviceSecret = "135918e694b8965c1853aa59b29c16b6"
mqttClientId = "k0y1pp87qA5.ECSdemo|securemode=2,signmethod=hmacsha256,timestamp=1711116493226|"
mqttUsername = "ECSdemo&k0y1pp87qA5"
mqttPassword = "49851d52ab3b33cec14fded74c95da9cdb7ecedfe2c3301b191b383181653c02"

# set timestamp, clientid, subscribe topic and publish topic
timeStamp = str((int(round(time.time() * 1000))))
subTopic = "/" + productKey + "/" + deviceName + "/user/reprec"
pubTopic = "/" + productKey + "/" + deviceName + "/user/controller"

# set host, port
host = productKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
# instanceId = "***"
# host = instanceId + ".mqtt.iothub.aliyuncs.com"
port = 1883

# set tls crt, keepalive
tls_crt = "/root/ca.crt"
keepAlive = 300

# calculate the login auth info, and set it into the connection options
client = mqtt.Client(mqttClientId)
client.username_pw_set(username=mqttUsername, password=mqttPassword)
client.tls_set(tls_crt)



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect aliyun IoT Cloud Sucess")
    else:
        print("Connect failed...  error code is:" + str(rc))

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print("receive message ---------- msg is : " + str(msg))
    print("receive message ---------- topic is : " + topic)
    print("receive message ---------- payload is : " + payload)

    if ("thing/service/property/set" in topic):
        on_thing_prop_changed(client, msg.topic, msg.payload)

def on_thing_prop_changed(client, topic, payload):
    post_topic = topic.replace("service","event")
    post_topic = post_topic.replace("set","post")
    Msg = json.loads(payload)
    params = Msg['params']
    post_payload = "{\"params\":" + json.dumps(params) + "}"
    print("reveice property_set command, need to post ---------- topic is: " + post_topic)
    print("reveice property_set command, need to post ---------- payload is: " + post_payload)
    client.publish(post_topic, post_payload)

def connect_mqtt():
    client.connect(host, port, keepAlive)
    return client

def publish_message(content):
    message = str(content)
    client.publish(pubTopic, message)
    print("publish msg: " + str(content))

def subscribe_topic():
    # subscribe to subTopic("/a1LhUsK****/python***/user/get") and request messages to be delivered
    client.subscribe(subTopic)
    print("subscribe topic: " + subTopic)

client.on_connect = on_connect
client.on_message = on_message

def command():
    client = connect_mqtt()
    client.loop_start()
    time.sleep(1)
    subscribe_topic()
    while True:
        publish_message(1)
        time.sleep(30)


command()

