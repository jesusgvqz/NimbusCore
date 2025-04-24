from flask import Blueprint, jsonify
from flasgger import swag_from

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/ping", methods=["GET"])
@swag_from({
    'responses': {
        200: {
            'description': 'Returns Pong!',
            'examples': {
                'application/json': {
                    'message': 'Pong!'
                }
            }
        }
    }
})
def ping():
    return jsonify({"message": "Pong!"})
