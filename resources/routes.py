from flask_restful import Api

from resources.healthcheck import HealthCheckResource


def set_routes(api: Api):
    api.add_resource(HealthCheckResource, '/health-check')