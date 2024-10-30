# app/app.py

from flask import Flask
from config import Config
from models import db
from routes import main  # Import the main Blueprint

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # Initialize db with the app

# Register the Blueprint
app.register_blueprint(main)

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
