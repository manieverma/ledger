from resources.base import BaseResource
from services.healthcheck import HealthCheckService


class HealthCheckResource(BaseResource):

    def get(self):
        service = HealthCheckService()
        return service.get_health_status()

    def put(self):
        return {"message":"connection complete"}