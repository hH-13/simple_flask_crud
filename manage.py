from flask_migrate import Migrate

from app import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    # os.environ["FLASK_APP"] = "manage.py"  # export FLASK_APP=manage.py
    app.run()
