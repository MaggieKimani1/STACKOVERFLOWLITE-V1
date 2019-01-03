from flask import Flask, Blueprint
from flask_restful import Api, Resource
from instance.config import app_config



def create_app(config_name):
  '''load the right configurations from config.py given a config name'''
  app = Flask(__name__, instance_relative_config=True) 
  app.config.from_object(app_config[config_name])

  '''Import and register the blueprint from the factory using app.register_blueprint()'''
  from .api.v1.views import api_v1 
  app.register_blueprint(api_v1)
  
  return app