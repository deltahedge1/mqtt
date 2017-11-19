import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("connected with result code"+str(rc))

    #subscribing in on_connect() - if we lose the connection
    #reconnect then subscriptions will be renewed

    client.subscribe("CoreElectronics/test")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))





client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 80)

client.loop_forever()
