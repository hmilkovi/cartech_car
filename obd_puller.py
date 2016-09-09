import obd
from obd import OBDStatus
import time
import json
import mqtt

connection = obd.OBD("/dev/ttyUSB0")  # auto-connects to USB or RF port

cmd = obd.commands.RPM
cmd1 = obd.commands.COOLANT_TEMP
cmd2 = obd.commands.SPEED
cmd3 = obd.commands.GET_DTC
cmd4 = obd.commands.MAF
mqttc = mqtt.MQTTClass()

connected = False
while not connected:
  try:
    mqtt_client = mqttc.run()
    connected = True
  except:
    connected = False

while(1):
    if connection.status() == OBDStatus.CAR_CONNECTED:
        response = connection.query(cmd)
        data = {'vin': 'WF0DXXGAJD7M04824', 'senzor': 'rpm', 'value': response.value }
        mqtt_client.publish("metric/rpm",json.dumps(data), 0)
        response = connection.query(cmd1)
        data = {'vin': 'WF0DXXGAJD7M04824', 'senzor': 'collant_temp', 'value': response.value }
        mqtt_client.publish("metric/collant_temp",json.dumps(data), 0)
        response = connection.query(cmd2)
        vss = response.value
        data = {'vin': 'WF0DXXGAJD7M04824', 'senzor': 'speed', 'value': response.value }
        mqtt_client.publish("metric/speed",json.dumps(data), 0)
        response = connection.query(cmd3)
        response = connection.query(cmd4)
        maf = response.value
        data = {'vin': 'WF0DXXGAJD7M04824', 'senzor': 'mpg', 'value': (vss * 7.718/maf) }
        mqtt_client.publish("metric/speed",json.dumps(data), 0)
    time.sleep(1)

