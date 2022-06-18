from flask_restful import Resource

from bootstrap.bus.message_bus import MessageBus
from bootstrap.main_bootstrap import bootstrap


class BaseResource(Resource):
    message_bus: MessageBus = bootstrap()

