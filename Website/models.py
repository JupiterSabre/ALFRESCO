from . import create_database, db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime



class User(db.Model, UserMixin, SerializerMixin):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # relationshup
    route_instances = db.relationship("Route_Instance", back_populates="user")


def get_current_date():
    return datetime.utcnow().strftime('%y-%m-%d')


class Route_Instance(db.Model, UserMixin, SerializerMixin):
    id= db.Column(db.Integer, primary_key=True)
    routedate = db.Column(db.String, nullable=False, default=get_current_date)
    latANDlong = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)

    # relationship
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="route_instances")

