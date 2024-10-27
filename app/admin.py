from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import Item, Role, User, db


class UserAdmin(ModelView):
    column_list = ("id", "email", "active", "roles", "items")
    form_columns = ("email", "password", "active", "roles", "items")


class RoleAdmin(ModelView):
    column_list = ("id", "name", "description")
    form_columns = ("name", "description")


class ItemAdmin(ModelView):
    column_list = ("id", "name", "description", "created_at", "user_id")
    form_columns = ("name", "description", "user_id")


def setup_admin(app):
    admin = Admin(app, name="MyApp Admin", template_mode="bootstrap4")
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(RoleAdmin(Role, db.session))
    admin.add_view(ItemAdmin(Item, db.session))
