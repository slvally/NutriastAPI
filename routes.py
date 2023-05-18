from flask import Blueprint
from functions import get_users, get_user, create_user, update_user, delete_user
from functions import get_intake_users, get_intake_user, create_intake_user, update_intake_user, delete_intake_user

def configure_routes(app, db_connection):
    users_bp = Blueprint('users_bp', __name__)
    app.register_blueprint(users_bp)
    users_bp.route('/users', methods=['GET'])(get_users(db_connection))
    users_bp.route('/users/<int:id>', methods=['GET'])(get_user(db_connection))
    users_bp.route('/users', methods=['POST'])(create_user(db_connection))
    users_bp.route('/users/<int:id>', methods=['PUT'])(update_user(db_connection))
    users_bp.route('/users/<int:id>', methods=['DELETE'])(delete_user(db_connection))

    intake_users_bp = Blueprint('intake_users_bp', __name__)
    app.register_blueprint(intake_users_bp)
    intake_users_bp.route('/intake_users', methods=['GET'])(get_intake_users(db_connection))
    intake_users_bp.route('/intake_users/<int:id>', methods=['GET'])(get_intake_user(db_connection))
    intake_users_bp.route('/intake_users', methods=['POST'])(create_intake_user(db_connection))
    intake_users_bp.route('/intake_users/<int:id>', methods=['PUT'])(update_intake_user(db_connection))
    intake_users_bp.route('/intake_users/<int:id>', methods=['DELETE'])(delete_intake_user(db_connection))