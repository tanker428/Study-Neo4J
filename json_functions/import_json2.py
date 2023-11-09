# import os
# import sys
# import json
# import pandas as pd
# from urllib.parse import urlparse


# parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if parent_dir not in sys.path:
#     sys.path.append(parent_dir)

# from concurrent.futures import ThreadPoolExecutor


# import time
# from neo4j import GraphDatabase

# class Neo4jConnection:
#     def __init__(self, uri, auth_type="basic", user=None, password=None, realm=None, parameters=None):
#         if auth_type == "basic":
#             self._driver = GraphDatabase.driver(uri, auth=(user, password))
#         elif auth_type == "none":
#             self._driver = GraphDatabase.driver(uri, auth=None)
#         elif auth_type == "custom":
#             self._driver = GraphDatabase.driver(uri, auth=AuthTokens.custom("my_scheme", user, password, realm=realm, parameters=parameters))
#         else:
#             raise ValueError(f"Unsupported auth_type: {auth_type}")

#     def close(self):
#         self._driver.close()

#     def run_query(self, query, parameters=None, database=None):
#         # Check if the query is empty or consists only of whitespace
#         if not query.strip():
#             return

#         with self._driver.session(database=database) as session:
#             result = session.run(query, parameters)
#             records = list(result)

#             if not records:
#                 pass
#             return records

#     def ensure_database_exists(self, database_name):
#         # Check if the database exists
#         databases = self.run_query("SHOW DATABASES")
#         if database_name not in [record["name"] for record in databases]:
#             # Create the database if it doesn't exist
#             self.run_query(f"CREATE DATABASE {database_name}")

#     def assert_database_exists(self, database_name):
#         # Check if the database exists
#         databases = self.run_query("SHOW DATABASES")
#         if database_name not in [record["name"] for record in databases]:
#             raise ValueError(f"Database '{database_name}' does not exist!")

#     def remove_database_if_exists(self, database_name):
#         # Check if the database exists
#         databases = self.run_query("SHOW DATABASES")
#         if database_name in [record["name"] for record in databases]:
#             # Drop the database if it exists
#             self.run_query(f"DROP DATABASE {database_name}")

#     def assert_database_not_exists(self, database_name):
#         # Check if the database exists
#         databases = self.run_query("SHOW DATABASES")
#         if database_name in [record["name"] for record in databases]:
#             raise ValueError(f"Database '{database_name}' already exists!")





# #-------------------------------------------------------------------------
# MAX_THREADS = 16
# uri         = "bolt://localhost:7687"

# def load_from_disk(filename):
#     with open(filename, 'r') as f:
#         return json.load(f)

# def load_into_neo4j(_id, _name, _desc):
#     global uri
#     conn = Neo4jConnection(uri, auth_type="none")

#     query = """
#     CREATE (o:Object {id: $id, name: $name, description: $description})
#     RETURN o
#     """
    
#     parameters = {
#         'id': _id,
#         'name': _name,
#         'description': _desc
#     }
#     # print(
#     # f"""
#     # id:          {_id}
#     # name:        {_name}
#     # description: {_desc}
#     # """)
#     conn.run_query(query, parameters)
#     conn.close()
#     return False


# def main(base_directory=None, uri=None, user=None, password=None):
#     base_directory = base_directory
#     processed_folder_path = os.path.join(base_directory, "processed")


#     X = 4096
#     OBJECTS = {}
#     for i in range(X):
#         obj = {
#             "id": i,
#             "name": f"Object_{i}",
#             "description": f"This is object number {i}"
#         }
#         OBJECTS[i] = obj
#     # print(OBJECTS)


#     # Use ThreadPoolExecutor with MAX_THREADS to process files in parallel
#     with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
#         futures = []
#         # for base_filename, url_filename in OBJECTS.items():
#         for _index, _object in OBJECTS.items():
#             _id   = _object.get('id', '')
#             _name = _object.get('name', '')
#             _desc = _object.get('description', '')
#             futures.append(executor.submit(load_into_neo4j, _id, _name, _desc))

#             for future in futures:
#                 result = future.result()


# if __name__ == "__main__":
#     main(sys.argv[0])