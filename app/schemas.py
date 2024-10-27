from marshmallow import fields, validate

from .extensions import ma
from .models import Item, Role, User


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    description = ma.auto_field()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # Allows marshmallow to create model instances on deserialization
        exclude = ("password",)  # Exclude password from serialized output

    id = ma.auto_field(dump_only=True)
    email = ma.auto_field(required=True, validate=validate.Email())
    password = fields.String(load_only=True, required=True)
    active = ma.auto_field()
    roles = fields.Nested(RoleSchema, many=True)
    items = fields.Nested("ItemSchema", many=True, exclude=("user",))  # Avoid circular references


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    description = ma.auto_field()
    created_at = ma.auto_field(dump_only=True)
    user = fields.Nested(UserSchema, only=("id", "email"), dump_only=True)  # Include limited user info
