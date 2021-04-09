from flask import Blueprint
from flask import current_app as app


# Blueprint Configuration
inventory_bp = Blueprint(
    'inventory_bp', __name__,
    template_folder='templates',
    static_folder='static'
)