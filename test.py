#!/usr/bin/env python3

from mqttCom import iot                                   # Custom Python Module to perfrom MQTT Tasks




class Coms():
	def __init__(self):
		self._config_mqtt_server_url =  "192.168.1.13"
		self._config_mqtt_server_port = 1883
		self._orders_sub_config = 'test/topic'
		self._config_mqtt_qos = 0
		iot.mqtt_publish(self._config_mqtt_server_url,self._config_mqtt_server_port,self._orders_sub_config,'holla',0)
		
def mqttPub(messageString):
	print('here at publishing')
	iot.mqtt_publish('192.168.1.13',1883,'warehouse/orders',messageString,0)

if __name__ == '__main__':
	com_object = Coms()
	#mqttPub
