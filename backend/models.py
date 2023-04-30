from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'my_db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


class Post(db.Document):
    title = db.StringField(required=True, max_length=200)
    content = db.StringField(required=True)
    author = db.StringField(required=True, max_length=50)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)


class User(db.Document):
    name = db.StringField(required=True, max_length=50)
    email = db.EmailField(required=True)
    password = db.StringField(required=True, min_length=8)


if __name__ == '__main__':
    app.run()
