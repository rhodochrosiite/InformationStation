# File to initialize the application

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Uncomment this in production
# application = app

# Load the views
from app import views, models, controllers

# Load the config file
app.config.from_object('config')