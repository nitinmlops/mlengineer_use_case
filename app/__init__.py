import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Ensure this pulls from environment variable
    db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:mysecretpassword@db:5432/postgres')
    print(f"SQLALCHEMY_DATABASE_URI: {db_uri}")  # Debug print
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)

    # Add retry logic here
    attempts = 5
    while attempts > 0:
        try:
            with app.app_context():
                db.create_all()
            break
        except OperationalError as e:
            print(f"OperationalError: {e}")
            attempts -= 1
            time.sleep(5)

    if attempts == 0:
        raise Exception("Could not connect to the database after several attempts.")

    from .routes import main
    app.register_blueprint(main)

    return app
