from app import marsh
from models.plant import PlantModel
from marshmallow import fields
from serializers.user import UserSerializer


class PlantSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = PlantModel
        load_instance = True
