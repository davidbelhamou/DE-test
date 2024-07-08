# Overview
This project demonstrates the use of file system monitoring and database operations in Python.
The codebase consists of three main functionalities implemented in separate threads:

1. Generating Fake Data: One thread is responsible for generating fake data files in a designated directory every 5 seconds.
2. Monitoring the Directory: Another thread uses the watchdog library to monitor the directory for new files and insert these files into an SQLite database based on their filenames.
3. Inserting Data into SQLite database

Design and Implementation:
- Generating Fake Data: This code generates fake JSON data for vehicle status and object detection, 
writes it to a specific directory with, and repeats this process every 5 seconds.
The data files are named based on the table they are intended to be inserted into,
indicating the appropriate database table.


- Monitoring the Directory
Utilizes the watchdog library to watch the data directory.
When a new file is detected, the MyHandler class handles the file creation event.
The handler reads the new file and inserts its data into the appropriate table.

filename convention:
<table_name>_timestamp.json

## Wy use watchdog?
watchdog library provides efficient and real-time file system event monitoring with minimal system resource usage,
making it ideal for lightweight and responsive applications. Its cross-platform compatibility and straightforward API

## Database choice
For the purposes of this exercise, SQLite was chosen for its simplicity and ease of implementation.
SQLite is a lightweight database that is easy to set up and use, making it ideal for quick development. 

In a real-world scenario, the choice of database would depend on the specific requirements of the application:

### Amazon Redshift: 
If the application requires complex queries and advanced analytics,
Amazon Redshift would be a suitable choice. 
Redshift is a fully managed data warehouse service that excels at handling large-scale data 

### MongoDB:
For applications that do not require complex queries and need to scale easily, 
MongoDB is an excellent option. MongoDB is a NoSQL database that is schema-less,
which means it can handle unstructured data without the overhead of defining and maintaining a rigid schema. 


## More
In this implementation, the two types of files are generated in the same directory. With more time,
I would separate them.
Also, for handling many more file types, I would consider using more threads or multiprocessing.

Other consideration would be about Indexing some fields, for better performance like timestamp fields.

# How to run

- git clone the repo
- cd to mobileye-interview directory
- run command python main.py