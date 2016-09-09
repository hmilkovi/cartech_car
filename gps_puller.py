#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading
import json

import mqtt

gpsd = None #seting the global variable

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start()
    time.sleep(6)
    mqttc = mqtt.MQTTClass()
    connected = False
    while not connected:
      try:
        mqtt_client = mqttc.run()
        connected = True
      except:
        connected = False
    while True:
      print gpsd.fix.latitude
      if gpsd.fix.latitude and gpsd.fix.longitude:
        gps_data = {'lat': gpsd.fix.latitude, 'long': gpsd.fix.longitude}
        data = {'vin': 'VNKJV18320A211146', 'senzor': 'gps', 'value': json.dumps(gps_data) }
        mqtt_client.publish("metric/gps",json.dumps(data), 0)

      time.sleep(0.5)

  except (KeyboardInterrupt, SystemExit):
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join()
  print "Done.\nExiting."