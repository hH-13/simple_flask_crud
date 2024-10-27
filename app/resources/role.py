from flask_restx import Resource, reqparse

from ..extensions import db
from ..models import Role
from ..schemas import RoleSchema

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# Define the request parser and its arguments
parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name of the role is required")
parser.add_argument("description", type=str, required=False, help="Description of the role")


class RoleResource(Resource):
    def get(self, id):
        role = Role.query.get_or_404(id)
        return role_schema.dump(role)

    def post(self):
        args = parser.parse_args()
        role = Role(name=args["name"], description=args.get("description"))
        db.session.add(role)
        db.session.commit()
        return role_schema.dump(role), 201

    def put(self, id):
        args = parser.parse_args()
        role = Role.query.get_or_404(id)
        role.name = args["name"]
        role.description = args.get("description")
        db.session.commit()
        return role_schema.dump(role)

    def delete(self, id):
        role = Role.query.get_or_404(id)
        db.session.delete(role)
        db.session.commit()
        return "", 204


class RoleListResource(Resource):
    def get(self):
        roles = Role.query.all()
        return roles_schema.dump(roles)
