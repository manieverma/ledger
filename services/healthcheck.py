from repository.healthcheck import HealthCheckRepository


class HealthCheckService:

    def __init__(self):
        self.health_repository = HealthCheckRepository()

    def get_health_status(self):
        response = self.health_repository.get_health_status()
        return response

