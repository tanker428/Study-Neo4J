import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface


"""
test create_json
"""
neo4j_interface = Neo4jInterface("bolt://localhost:7687", "try", "vrwiki81")
neo4j_interface.delete_all_node()
# neo4j_interface.json_to_3node_graph(json_path="data/sample_vr_data.json")

json_path = "data/sample_vr_data.json"
json_path_nishi = "data/user-nishi-dict.json"
json_path_example = "data/example.json"
json_path_sample = "data/sample_西.json"
json_ontology_ver1 = "data/user-nishi-dict.json"
json_example = "data/sample_ontology_ver1.json"
number = 1


neo4j_interface.delete_all_node()
neo4j_interface.json_to_allnode_graph(json_path=json_ontology_ver1, ontology_number=number)

# neo4j_interface.json_to_allnode_graph(json_path=json_path_nishi)

