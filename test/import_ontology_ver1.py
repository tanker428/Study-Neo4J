import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

graph = Neo4jInterface("bolt://localhost:7687", name = "try", password='vrwiki81')

json_ontology_ver1 = "data/sample_ontology_ver1"

# graph.json_to_allnode_graph(json_path=json_ontology_ver1)

label = "Object"
name = "Talisman_Word10" 

graph.check_if_node_exist(label, name)