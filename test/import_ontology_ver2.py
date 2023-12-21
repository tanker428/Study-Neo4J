import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

graph = Neo4jInterface("bolt://localhost:7687", name = "try", password='vrwiki81')

json_ontology_ver1 = "data/user-nishi-dict.json"
json_example = "data/sample_ontology_ver1.json"
number = 2

flame = "043560"
timestamp = "20230829134625"
label = "Bbox"

graph.delete_all_node()
graph.set_before_flame()
graph.json_to_allnode_graph(json_path=json_ontology_ver1, ontology_number=number)

graph.check_if_node_exist_flame_timestamp(label, flame, timestamp)
