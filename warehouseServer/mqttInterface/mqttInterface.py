from flask import Blueprint,redirect,url_for, session
from flask import current_app as app
import time
from flask import request
from mqttCom import iot
#from flask import 

mqttBroker = app.config['MQTT_BROKER_URL']

mqttTopic = app.config['MQTT_ORDER_TOPIC']
mqttPort = app.config['MQTT_BROKER_PORT']
mqttQos = app.config['MQTT_QOS']

# Blueprint Configuration
mqttInterface_bp = Blueprint(
	'mqttInterface_bp', __name__,
	template_folder='templates',
	static_folder='static'
)


def uuidGenerator():
	uuid1 = str(int(time.time()))[:6]
	return uuid1

def mqttPub(messageString):
	print('here at publishing {}'.format(messageString))
	ret = iot.mqtt_publish(mqttBroker,mqttPort,mqttTopic,messageString,0)
	print(ret)

@mqttInterface_bp.route('/mqtt', methods=['GET'])
def home():
	return'{}'.format(app.config['MQTT_PASSWORD'])

@mqttInterface_bp.route('/mqtt/talk/<orderBool>', methods=['POST'])
def jsonDump(orderBool):
	print(session)
	#orderBool = False
	'''
		request_data = request.get_json()	

		if orderBool=="False":
			if 'message' in request_data:
				print('mqtt')
				message = request_data['message']
				mqttPub(message)
				print('mqtt')
				return "Custom order Placed, Order info is {}".format(message)
			else:
				return'json invalid'
		else:
			print('doesnt make sense')
	'''			
		
	if request.method == 'POST':
		print('mqtt')
		if orderBool=="True":
			message = session['orderInfo']
			session.pop('orderInfo',None)
			mqttPub(str(message))
			return "Order Placed, Order info is {}".format(message)
		else:
			print('orderbool error')
	else:
		return'request_data error'
	


	

	