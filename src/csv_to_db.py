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
    if not data:
        raise ValueError('Data must not be empty')
    
    db = TinyDB(db_path)
    db.insert_multiple(data)
def query_db(db_path, query_field, query_value):
    db = TinyDB(db_path)
    User = Query()
    
    if query_field and query_value:
        results = db.search(User[query_field] == query_value)
    else:
        results = db.all()
    
    print(f"Found {len(results)} matching records.")
    return results

if __name__ == "__main__":
    # Main execution logic
    pass