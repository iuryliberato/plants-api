from marshmallow import fields
from app import mash
from models.users import UserModel


class UserSerializer(mash.SQLAlchemyAutoSchema):

    password = fields.String(required=True)

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("password_hash", "email")
