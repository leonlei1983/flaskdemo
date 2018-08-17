from flask import Blueprint
from flask_restplus import Api

from apis.namespace1 import api as ns1

blueprint = Blueprint('api3', __name__, url_prefix='/api/3')
api = Api(blueprint,
    title='My Title',
    version='3.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1)
# api.add_namespace(ns1, path='/prefix/of/ns1')
