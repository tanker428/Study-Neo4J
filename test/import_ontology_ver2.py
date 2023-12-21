import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

graph = Neo4jInterface("bolt://localhost:7687", name = "try", password='vrwiki81')

json_ontology_ver1 = "data/user-nishi-dict.json"
json_example = "data/sample_ontology_ver1.json"
number = 2


graph.delete_all_node()
graph.json_to_allnode_graph(json_path=json_ontology_ver1, ontology_number=number)


