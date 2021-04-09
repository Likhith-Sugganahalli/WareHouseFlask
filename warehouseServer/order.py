#from models.database import db
from . import db

class order(db.Model):
	__tablename__ = 'Orders'
	__table_args__ = {'sqlite_autoincrement': True}
	Product = db.Column(db.String(80), unique=False, nullable=False)
	OrderId = db.Column(db.String(10), unique=True, nullable=False)

	SrNo =db.Column(db.Integer, primary_key=True)

	Quantity =db.Column(db.Integer,nullable=False)

	def __repr__(self):
		return "<Title: {}>".format(self.OrderId)

