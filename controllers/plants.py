# Here is my controller for plants

# ! Blueprint is Flask's router.
# ! import request to get request information sent by the user.
from flask import Blueprint, request

# ! Import our temporary db
from models.temp_data import temp_db

from serializers.plant import PlantSerializer

from app import db

from models.plant import PlantModel

plant_serializer = PlantSerializer()

# ! Creating a instance of our Blueprint class, with the controller name and __name__
router = Blueprint("plants", __name__)


# TODO Get all the plants
# ! We need a decorator to specify the route.
@router.route("/plants", methods=["GET"])
def get_plants():
    plants = db.session.query(PlantModel).all()
    return plant_serializer.jsonify(plants, many=True)


# TODO Get a plant by its ID
@router.route("/plants/<int:plant_id>", methods=["GET"])
def get_single_plant(plant_id):
    plant = db.session.query(PlantModel).get(plant_id)
    if not plant:
        return {"message": "not found plant"}
    return plant_serializer.jsonify(plant)


# TODO Add a new plant
@router.route("/plants", methods=["POST"])
def create():
    plant_dictionary = request.hson
    plant_model = plant_serializer.load(plant_dictionary)
    plant_model.user_id = 1
    db.session(plant_model)
    db.session.commit()
    return plant_serializer.jsonify(plant_model)


# TODO Update a plant


@router.route("/teas/‹int:tea id›", methods=["PUT"])
def update_single_tea(plant_id):

    existing_plant = db.session.query(PlantModel).get(plant_id)

    plant_dictionary = request.json

    plant = plant_serializer.load(
        plant_dictionary, instance=existing_plant, partial=True
    )

    db.session.add(plant)
    db.session.commit(plant)

    return plant_serializer.jsonify(plant)


# TODO Delete a plant
@router.route("/plants/<int:plant_id>", methods=["DELETE"])
def delete_single_plant(plant_id):
    plant = db.session.query(PlantModel).get(plant_id)

    db.session.delete(plant)
    db.session.commit()

    return plant_serializer.jsonify(plant)
