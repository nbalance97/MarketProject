# from Settings import db
from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    contents = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_name = db.Column(db.String(80), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship(User, foreign_keys=author_id, post_update=True)


