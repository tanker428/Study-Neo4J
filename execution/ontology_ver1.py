import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface


"""
create_ontology_ver1 
"""
neo4j_interface = Neo4jInterface("bolt://localhost:7687", "ontology-ver1", "vrwiki81")

json_ontology_ver1 = "data/user-nishi-dict.json"
number = 1

# 前のグラフを消去
neo4j_interface.delete_all_node()

# 生成する
neo4j_interface.json_to_allnode_graph(json_path=json_ontology_ver1, ontology_number=number)