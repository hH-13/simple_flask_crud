from flask_restx import Api

from .item import ItemResource
from .user import UserResource


def register_resources(api: Api):
    api.add_resource(ItemResource, "/items/<int:id>")
    api.add_resource(UserResource, "/users/<int:user_id>", "/users")
