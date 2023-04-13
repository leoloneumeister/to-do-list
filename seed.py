from app.app import create_app
from app.todo.models import User
from app.cookies.models import Cookie
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()


cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': 1.50},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': 1.00},
  'sugar' : {'name': 'Sugar', 'price': 0.75},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': 0.50},
  'oatmeal' : {'name': 'Oatmeal', 'price': 0.25},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': 1.00},
}

for slug, cookie in cookies_data.items():
  new_cookie = Cookie(slug=slug, name=cookie['name'], price=cookie['price'])
  db.session.add(new_cookie)

db.session.commit()




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