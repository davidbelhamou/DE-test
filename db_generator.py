import sqlite3
from configuration.config import logger


def init_db():
    try:
        conn = sqlite3.connect('streaming_objects_vehicles.db')
        cursor = conn.cursor()
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS objects_detection (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id TEXT NOT NULL,
                detection_time DATETIME NOT NULL,
                object_type TEXT NOT NULL,
                object_value INTEGER NOT NULL
            );
             CREATE TABLE IF NOT EXISTS vehicles_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id TEXT NOT NULL,
                report_time DATETIME NOT NULL,
                status TEXT NOT NULL
                )
        ''')
        conn.commit()
        conn.close()
    except Exception as ex:
        logger.error(f'Failed creating db, error: {ex}')


def insert_rows(data: list, table_name: str):
    columns_by_table = {'vehicles_status': ('id', 'vehicle_id', 'report_time', 'status'),
                        'objects_detection': ('id', 'vehicle_id', 'detection_time', 'object_type', 'object_value')}
    # Create a string of placeholders for the values, e.g., '?, ?, ?, ?'
    if table_name in columns_by_table:
        cols = ','.join(['?' for _ in range(len(columns_by_table[table_name]))])

        try:
            conn = sqlite3.connect('streaming_objects_vehicles.db')
            cursor = conn.cursor()
            data_tuples = []
            columns = columns_by_table[table_name]
            # Prepare the data as a list of tuples
            for record in data:
                data_tuples.append(tuple(record[col] if col in record else None for col in columns))

            cursor.executemany(f'INSERT INTO {table_name} {columns_by_table[table_name]} VALUES ({cols})', data_tuples)
            conn.commit()
            conn.close()
        except Exception as ex:
            logger.error(f'Failed INSERT INTO {table_name}, error: {ex}')
    else:
        raise Exception(f'{table_name} does not exist')
