from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.user import User

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("", methods=["GET"])
def index():
    users = User.query.all()

    return jsonify([
        {
            "id": user.id,
            "name": user.name,
        }
        for user in users
    ])


@bp.route("", methods=["POST"])
def create():
    data = request.get_json()

    user = User(name=data["name"])
    user.password = data["password"]

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "name": user.name,
    }), 201


@bp.route("/<int:user_id>", methods=["GET"])
def show(user_id):
    user = db.get_or_404(User, user_id)

    return jsonify({
        "id": user.id,
        "name": user.name,
    })


@bp.route("/<int:user_id>", methods=["PATCH"])
def update(user_id):
    user = db.get_or_404(User, user_id)
    data = request.get_json()

    if "name" in data:
        user.name = data["name"]

    db.session.commit()

    return jsonify({
        "id": user.id,
        "name": user.name,
    })


