import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface

# Neo4jInterfaceはsearchのクラスを引き継いでいる
example = "example-py2neo"
normal = "try"
graph = Neo4jInterface("bolt://localhost:7687", name = normal, password='vrwiki81')

label = "Object"
graph.search_node_label(label)

node = graph.search_node_objectname_label("Object", "Booze_Word8")
# node = graph.search_node_name("Booze_Word8")

relation_name = ":mainObject"
name = "Booze_Word8"
graph.search_relationship(node, relation_name)
graph.example()

# graph.example()



