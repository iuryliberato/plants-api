from app import db

from models.users import UserModel


# ! This will create a SQLAlchemy model, extending the db.Model
class PlantModel(db.Model):

    # ! Override the default name of the table to be something a bit nicer
    __tablename__ = "plants"

    # ! This is going to be the unique ID for this model.
    id = db.Column(db.Integer, primary_key=True)

    # ! Here are the other fields for our tea, each wil be its own column in the db.
    name = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    db.relationship("UserModel", backred="plants")
