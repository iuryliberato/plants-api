from sqlalchemy.ext.hybrid import hybrid_property

from flask_bcrypt import bcrypt

from app import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.column(db.Text, nullable=False, unique=True)
    email = db.column(db.Text, nullable=False, unique=True)
    password_hash = db.column(db.Text, nullable=True)

    user_id = db.column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):

        encoded_hashed_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_hashed_pw.decode("utf-8")

    def validate_password(self, login_password):
        return bcrypt.check_password_hash(self.password_hash, login_password)
