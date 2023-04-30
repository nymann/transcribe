from transcribe.api import Api
from transcribe.core.config import Config
from transcribe.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
