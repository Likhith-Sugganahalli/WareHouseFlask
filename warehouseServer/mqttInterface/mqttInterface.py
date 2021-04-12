from flask import Blueprint,redirect,url_for
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

@mqttInterface_bp.route('/mqtt/talk/')
def redirectingPages():
	return redirect(url_for('mqttInterface_bp.jsonDump',orderBool = False))


def uuidGenerator():
	uuid1 = str(int(time.time()))[:6]
	return uuid1

def mqttPub(messageString):
	iot.mqtt_publish('192.168.1.14',1883,'warehouse/orders',messageString,0)


@mqttInterface_bp.route('/mqtt', methods=['GET'])
def home():
	return'{}'.format(app.config.keys())

@mqttInterface_bp.route('/mqtt/talk/tome', methods=['GET','POST'])
def jsonDump():
	orderBool = False

	if request.method == 'POST':
		request_data = request.get_json()

		if request_data:

			if orderBool == False:
				if 'message' in request_data:
					message = request_data['message']
					mqttPub(message)
					return "Custom order Placed, Order info is {}".format(message)
				else:
					return'json invalid'
			else:
				message = session['orderInfo']
				session.pop('orderInfo',none)
				mqttPub(message)
				return "Order Placed, Order info is {}".format(message)
		return'some error'
	else:
		return'no gets here'


	

	