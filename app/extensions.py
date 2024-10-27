from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
security = Security()
