from flask import Blueprint
from flask_restplus import Api

from apis.namespace1 import api as ns1

blueprint = Blueprint('api2', __name__, url_prefix='/api/2')
api = Api(blueprint,
    title='My Title',
    version='2.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
# api.add_namespace(ns1, path='/prefix/of/ns1')
