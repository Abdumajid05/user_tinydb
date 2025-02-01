import csv
from tinydb import TinyDB, Query

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found.")
    

def insert_into_db(data, db_path):
    # Insert data into TinyDB
    pass

def query_db(db_path, query_field, query_value):
    # Query the database
    pass

if __name__ == "__main__":
    # Main execution logic
    pass