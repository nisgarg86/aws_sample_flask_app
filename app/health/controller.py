"""
contains application health check
"""

from flask import Blueprint

health_module = Blueprint('health', __name__, url_prefix='/health')


@health_module.route('/', methods=['GET'])
def get_health_status():
    return {
            'status': 'healthy',
            'version': 0.1
            }
