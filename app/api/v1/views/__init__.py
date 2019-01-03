from flask import Blueprint
from flask_restful import Api, Resource

# import the endpoint classes


# create the app Blueprint named app_v1, defined under __name__ using /api/v1 as the prefix for all urls associated with the bp
app_v1 = Blueprint('app_v1',__name__, url_prefix="/api/v1")
api_v1 = Api(app_v1)

# add resources to the app Blueprint
