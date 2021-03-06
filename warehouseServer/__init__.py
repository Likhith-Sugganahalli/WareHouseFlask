"""Initialize Flask app."""
from flask import Flask

import os
#from warehouseServer.models.database import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    db.init_app(app)

    

    with app.app_context():
        # Import parts of our application
        #db.create_all()

        from .webInterface import webInterface
        from .mqttInterface import mqttInterface
        from .inventory import inventory

        # Register Blueprints
        app.register_blueprint(webInterface.webInterface_bp)
        app.register_blueprint(mqttInterface.mqttInterface_bp)
        #app.register_blueprint(inventory.inventory_bp)

        db.create_all()



        return app



