from flask import Blueprint
from flask import current_app as app
import time
from flask import request
from mqttCom import iot
#from flask import 

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
	iot.mqtt_publish('192.168.1.14',1883,'warehouse/orders',messageString,0)


@mqttInterface_bp.route('/mqtt', methods=['GET'])
def home():
	return'Hi'

@mqttInterface_bp.route('/mqtt/talk/', methods=['POST'])
def jsonDump():
	request_data = request.get_json()

	if request_data:
		if 'message' in request_data:
			message = request_data['message']
		else:
			return'json invalid'
	mqttPub(message)

	return "Order Placed, Order info is {}".format(message)