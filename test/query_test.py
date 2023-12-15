from py2neo import Graph

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from query_functions.query_functions import Search
from json_functions.neo4jinterface import Neo4jInterface

# my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')
# my_graph.nodes.match()
# print(type(my_graph))

graph_search = Search("bolt://localhost:7687", name = "example-py2neo", password='vrwiki81')
graph_create = Neo4jInterface("bolt://localhost:7687", user = "example-py2neo", password='vrwiki81')

graph_search.search_node_name("Tom Hanks")
# a = graph_search.search_node_label("Person")
# print(len(a))
graph_search.search_node_name_label("Person", "Tom Hanks")
# graph_search.search_node_label_number("Person", 10)

old_node = graph_search.search_node_label_name_with_query("Person", "Tom Hanks")
old_node2 = graph_search.search_node_label_name_with_query("Person", "Keanu Reeves")
# old_node["baka"] = 1
baka_dict = {"baka":3}
graph_search.add_node_property(old_node, baka_dict)
graph_search.search_node_label_name_with_query("Person", "Tom Hanks")

# できたけどcypher queryだと新しいnodeで作ってる
# graph_search.add_2node_relationship()
graph_create.old_node_relationship(old_node, old_node2)

