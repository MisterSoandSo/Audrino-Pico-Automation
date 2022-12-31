from backend import *
from secrets import *
from machine import Pin, I2C

#MQTT Client Login 
mqtt_ip = secrets['mqtt_server']
mqtt_user=secrets['mqtt_user']
mqtt_password=secrets['mqtt_pswd']

try:
    mq_connect(ssid=secrets['ssid'],psk=secrets['password'])
    client = mqtt_connect(client_id = 'picow',mqtt_server = mqtt_ip, user = mqtt_user,password = mqtt_password)
except OSError as e:
    reconnect()


while True:
    #Read Sensor Data



    #Publish as MQTT payload
    client.publish('', )
    time.sleep(30)