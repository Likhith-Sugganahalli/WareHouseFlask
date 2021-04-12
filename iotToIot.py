#!/usr/bin/env python3

from mqttCom import iot
import ast

class Coms():
	def __init__(self):
		self._config_mqtt_server_url =  "192.168.1.13"
		self._config_mqtt_server_port = 1883
		#self._orders_sub_config = 'warehouse/orders'
		self._orders_sub_config = 'test/topic'
		self._config_mqtt_qos = 0


		ret = iot.mqtt_subscribe_thread_start(self.mqtt_sub_callback,self._config_mqtt_server_url,self._config_mqtt_server_port,self._orders_sub_config,self._config_mqtt_qos)
		print('thread started {}'.format(ret))

	def mqtt_sub_callback(self, client, userdata, message):
		payload = str(message.payload.decode("utf-8"))
	
		print("[MQTT SUB CB] Message: ", payload)
		print("[MQTT SUB CB] Topic: ", message.topic)

if __name__ == '__main__':
	com_object = Coms()
	while True:
		pass
