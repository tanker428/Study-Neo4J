import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

"""
 create_ontology_ver2 graph
"""

neo4j_interface = Neo4jInterface("bolt://localhost:7687", "nishiBver2", "vrwiki81")

# 前のグラフを消去する
neo4j_interface.delete_all_node()

# 入力
json_ontology_ver2 = "data/user-nishi-B-dict.json"
number = 2

#　準備
neo4j_interface.set_before_flame()

neo4j_interface.json_to_allnode_graph(json_path=json_ontology_ver2, ontology_number=number)