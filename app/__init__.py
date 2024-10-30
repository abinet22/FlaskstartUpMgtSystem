from flask import Flask
from .models import db  # Import the db instance from models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your preferred database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize the db with the app

    with app.app_context():
        db.create_all()  # Create database tables

    return app
