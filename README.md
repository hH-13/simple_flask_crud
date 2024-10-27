# Quick Setup

```bash
git clone https://github.com/hH-13/simple_flask_crud.git
cd simple_flask_crud

poetry shell
poetry install

flask db init
flask db migrate
flask db upgrade

flask run --debug
```

Access the application at: `http://localhost:5000`

<!-- ## API Endpoints

- GET `/api/items` - List all items
- GET `/api/items/<id>` - Get a specific item
- POST `/api/items` - Create a new item
- PUT `/api/items/<id>` - Update an item
- DELETE `/api/items/<id>` - Delete an item -->

### Database Migrations

If you encounter database migration issues:
```bash
flask db stamp head
flask db migrate
flask db upgrade
```

