import os
import json
from dataclasses import dataclass
import logging
from pathlib import Path


@dataclass
class Route:
    route_to_survey: str
    file_pattern: str


class Configuration:
    DEFAULT_CONFIG_PATH = './configuration/config.json'

    def __init__(self, config_path: str | Path = DEFAULT_CONFIG_PATH) -> None:
        self.__config_json_path = os.getenv('CONFIG_PATH', self.DEFAULT_CONFIG_PATH)  # Use ConfigMap in prod
        with open(self.__config_json_path, 'r') as reader:
            config_json = json.load(reader)
        self.configuration = config_json

    @property
    def create_object_detection_route(self):
        # Extract from the config.json file the items for object_sdetection
        conf_dict = {key: val for key, val in self.configuration['object_detection'].items() if
                     key in Route.__annotations__}
        return Route(**conf_dict)

    @property
    def create_vehicles_status_route(self):
        # Extract from the config.json file the items for vehicles_status
        conf_dict = {key: val for key, val in self.configuration['vehicles_status'].items() if
                     key in Route.__annotations__}
        return Route(**conf_dict)


# Configure basic logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger('MyLogger')
