import paho.mqtt.publish as publish

for i in range(10):
    publish.single("CoreElectronics/test", "hello", hostname="iot.eclipse.org")

