import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

graph = Neo4jInterface("bolt://localhost:7687", name = "example-py2neo", password='vrwiki81')

add_rel = graph.search_node_name_label("User", "nishi")

node_name = "Ben Miles"
destination_name = "Bill Paxton"
rel = "nishi"

graph.old_node_relationship(node_name, destination_name, rel)
