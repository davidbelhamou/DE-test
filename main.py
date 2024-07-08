import os
import sqlite3
from fake_data_generator import generate_data
from configuration.config import Configuration, logger
from pathlib import Path
from watcher import monitor_directory
from db_generator import init_db
import threading

if __name__ == '__main__':
    # initialize the db + configuration
    init_db()
    conf = Configuration()
    # Create the 2 Thread, one for generating data the other one to monitor the specific directory
    generator_data = threading.Thread(target=generate_data.main, args=(conf,))
    watcher_data = threading.Thread(target=monitor_directory, args=(conf.create_vehicles_status_route,))
    logger.info('Start Main prog')
    watcher_data.start()
    generator_data.start()
    generator_data.join()
    watcher_data.join()

