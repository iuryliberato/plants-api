from flask import Blueprint, request
from marshmallow.exceptions import ValidationError
from app import db
from serializers.user import UserSerializer
from http import HTTPStatus
from models.users import UserModel

user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup():
    try:
        user_dictionary = request.json

        user_model = user_serializer.load(user_dictionary)
        db.session.add(user_model)
        db.session.commit()
        return user_serializer.jsonify(user_model)

    except ValidationError as e:
        return {"errors": e.message, "message": "something went wrong"}
    except Exception as e:
        return {"message": "something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("login", methods=["POST"])
def login():
    credentials_dictionary = request.json
    user = (
        db.session.query(UserModel)
        .filter_by(email=credentials_dictionary["email"])
        .first()
    )

    if not user:
        return {"message": "Login failed"}
    if not user.validate_password(credentials_dictionary["password"]):
        return {"message": "login failed, Try again."}

    print("success")

    pass
