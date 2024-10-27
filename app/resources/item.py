from flask_restx import Resource, reqparse

from ..extensions import db
from ..models import Item

parser = reqparse.RequestParser()
parser.add_argument("name", required=True)
parser.add_argument("description", required=True)


class ItemResource(Resource):
    def get(self, id):
        item = Item.query.get_or_404(id)
        return {"id": item.id, "name": item.name, "description": item.description}

    def post(self):
        args = parser.parse_args()
        item = Item(name=args["name"], description=args["description"])
        db.session.add(item)
        db.session.commit()
        return {"id": item.id, "name": item.name, "description": item.description}, 201

    def put(self, id):
        args = parser.parse_args()
        item = Item.query.get_or_404(id)
        item.name = args["name"]
        item.description = args["description"]
        db.session.commit()
        return {"id": item.id, "name": item.name, "description": item.description}

    def delete(self, id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return "", 204
