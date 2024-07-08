import json
import time
from datetime import datetime, timezone
from uuid import uuid4
from pathlib import Path
import numpy as np
import random
from configuration.config import Configuration


def generate_fake_object_detection_data(route_path: Path, num_records: int = 3) -> None:
    data = []
    for _ in range(num_records):
        record = {
            "vehicle_id": str(uuid4()),
            "detection_time": datetime.now(timezone.utc).isoformat(),
            "object_type": random.choices(("pedestrians", "vehicles", "bicycles"))[0],
            "object_value": np.random.randint(low=1, high=4)
        }
        data.append(record)
    return write_json_file(data, 'objects_detection', route_path)


def generate_fake_vehicles_status_data(route_path: Path, num_records: int = 3):
    data = []
    for _ in range(num_records):
        record = {
            "vehicle_id": str(uuid4()),
            "report_time": datetime.now(timezone.utc).isoformat(),
            "status": random.choices(("driving", "accident", "parking"))[0],
        }
        data.append(record)
    return write_json_file(data, 'vehicles_status', route_path)


def write_json_file(data: list, filename_suffix: str, path: Path):
    filename = filename_suffix + '_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.json'
    with open(path / filename, 'w') as writer:
        json.dump(data, writer, indent=4)


def main(conf: Configuration):
    # continuously generate fake data file
    while True:
        data_dir = Path(conf.create_vehicles_status_route.route_to_survey)
        data_dir.mkdir(parents=True, exist_ok=True)
        generate_fake_vehicles_status_data(data_dir)
        generate_fake_object_detection_data(data_dir)
        time.sleep(5)

