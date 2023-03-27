from app.extensions.database import db


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String())

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  email = db.Column(db.String(80))
  password = db.Column(db.String(80))