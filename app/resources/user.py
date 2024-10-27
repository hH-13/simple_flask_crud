# from flask_restx import Resource, reqparse

# from ..extensions import db
# from ..models import User

# parser = reqparse.RequestParser()
# parser.add_argument("email", required=True)
# parser.add_argument("password", required=True)


# class UserResource(Resource):
#     def get(self, id):
#         user = User.query.get_or_404(id)
#         return {"id": user.id, "email": user.email}

#     def post(self):
#         args = parser.parse_args()

#         user = User(email=args["email"], password=args["password"])
#         db.session.add(user)
#         db.session.commit()
#         return {"id": user.id, "email": user.email}, 201

#     def put(self, id):
#         args = parser.parse_args()

#         user = User.query.get_or_404(id)
#         user.email = args["email"]
#         user.password = args["password"]
#         db.session.commit()
#         return {"id": user.id, "email": user.email}

#     def delete(self, id):
#         user = User.query.get_or_404(id)
#         db.session.delete(user)
#         db.session.commit()
#         return "", 204

import uuid

from flask import request
from flask_restx import Resource
from werkzeug.security import generate_password_hash

from ..models import User, db
from ..schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if User.query.filter_by(email=email).first():
            return {"message": "User with this email already exists"}, 400

        new_user = User(email=email, password=generate_password_hash(password), fs_uniquifier=str(uuid.uuid4()))
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()

        user.email = data.get("email", user.email)
        if "password" in data:
            user.password = generate_password_hash(data["password"])
        user.active = data.get("active", user.active)

        db.session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return "", 204
