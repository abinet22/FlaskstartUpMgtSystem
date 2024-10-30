
from flask import Blueprint, render_template
from models import db, User

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/login')
def login():
    return render_template('login.html')
@main.route('/pricing')
def pricing():
    return render_template('pricing.html')
@main.route('/features')
def features():
    return render_template('features.html')
@main.route('/solutions')
def solutions():
    return render_template('solutions.html')

@main.route('/test-db')
def test_db():
    try:
        db.create_all()  # Ensure tables are created
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"
