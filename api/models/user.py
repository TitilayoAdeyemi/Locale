from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locale.db"

db.init_app(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(50), nullable = False, unique=True)
    password_hash = db.Column(db.Text(), nullable = False)

    
    def __repr__(self):
        return f"<User {self.username}>"
    

    def save(self):
        db.session.add(self)
        db.session.commit()


    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)