from flask import Blueprint, render_template, session, redirect, url_for
from flask import current_app as app
import time
from flask import request
from warehouseServer.order import db, order
#from flask import 


# Blueprint Configuration
webInterface_bp = Blueprint(
	'webInterface_bp', __name__,
	template_folder='templates',
	static_folder='static'
)




@webInterface_bp.route('/order/', methods=['POST'])
def jsonDump():

	jsonKeysList= ['productId','quantity'] 
	request_data = request.get_json()

	#orderInfoDict = {}



	if request_data:
		temp = {}
		for i in jsonKeysList:
			if i in request_data:
				temp[i] = request_data[i]
			else:
				return('json data invalid at {}'.format(temp))

		ttemp = uuidGenerator()
		temp['orderId'] = ttemp
		neworder = order(Product = temp['productId'],Quantity = temp['quantity'],OrderId = temp['orderId'])#,SrNo = 1)
		print("temp")
		db.session.add(neworder)  # Adds new User record to database
		db.session.commit()
		print("temp")
		session['orderInfo'] = temp
		print("temp")
		return redirect(url_for('mqttInterface_bp.jsonDump',orderBool = "True"))


	#return "Order Placed, Order info is {}".format(temp)


@webInterface_bp.route('/', methods=['GET'])
def home():
	 return render_template(
        'orderslist.jinja2',
        orders=order.query.all(),
        title="Show Users"
    )
def uuidGenerator():
	return str(int(time.time()))[6:]