# ! Connect to the database, then print "Success!" and disconnect
# ! Import the app, db
from app import app, db

from models.users import UserModel

# ! Import the tea
from models.plant import PlantModel

# ! This code will:
# ! - Run some code to connect to the db before our code
# ! - Run some code to disconnect after our code ends.
with app.app_context():

    try:
        print("Connected to our database!")
        # ! Delete all the tables on the database
        db.drop_all()
        # ! Create the tables on the database
        db.create_all()
        iury = UserModel(
            username="iury", email="iury@me.com", password_hash="mypassword"
        )
        db.session.add(iury)
        db.session.commit()
        # ! Creates the chai
        rose = PlantModel(
            name="Rose",
            description="description rose here",
            rating=4,
            in_stock=True,
            user_id=iury.id,
        )
        # ! We now need to save this to the db
        db.session.add(rose)
        db.session.commit()

        print("Seeding some data..")

    except Exception as e:
        print(e)
