import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

graph = Neo4jInterface("bolt://localhost:7687", name = "try", password='vrwiki81')

json_ontology_ver1 = "data/user-nishi-dict.json"
json_example = "data/sample_ontology_ver1.json"
number = 1


graph.delete_all_node()
graph.json_to_allnode_graph(json_path=json_ontology_ver1, ontology_number=number)

label = "Object"
name = "Booze_Word8"
flame = "001260" 

# graph.check_if_node_exist(label, name)
# print("check")
# graph.search_node_name_label_flame(label, name, flame)
