from app.app import create_app
from app.todo.models import User
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

users = {
  "user1": {
    "name": "leolo",
    "email": "leolo@gmail.com",
    "password": "dings"
  },
  "user2": {
    "name": "justin",
    "email": "justing@gmail.com",
    "password": "doings"
  },
  "user3": {
    "name": "lennart",
    "email": "lennart@gmail.com",
    "password": "dongs"
  },
}

for slug, user in users.items():
  new_user = User(name=user["name"], email=user["email"], password=user["password"])
  db.session.add(new_user)

db.session.commit()