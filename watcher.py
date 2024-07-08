import json

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from configuration.config import logger
from db_generator import insert_rows
from configuration.config import Route
import re
from pathlib import Path


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.new_files = []

    def on_created(self, event):
        print(f'File {event.src_path} has been created')
        prefix = re.match(r'(.*)_(\d{8}_\d{6})\.json', Path(event.src_path).name).group(1)
        with open(event.src_path, 'r') as reader:
            data = json.load(reader)
        insert_rows(data, prefix)


def monitor_directory(route: Route):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=route.route_to_survey, recursive=True)
    logger.info(f'Start WatchDog on directory: {route.route_to_survey}')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
