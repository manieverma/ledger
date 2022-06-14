from flask_restful import Resource


class BaseResource(Resource):
    message_bus = None

