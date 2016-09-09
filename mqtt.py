import paho.mqtt.client as mqtt
import ssl
import os


class MQTTClass:

    def __init__(self, clientid=None):
        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def mqtt_on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self._mqttc.username_pw_set('cartech', 'bAyDzaSW6')
        self._mqttc.connect("hrvoje.kraken.hr", 1883, 60)
        self._mqttc.loop_start()
        return self._mqttc
