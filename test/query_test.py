import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from query_functions.query_functions import Search

# my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')
# my_graph.nodes.match()
# print(type(my_graph))

graph_search = Search("bolt://localhost:7687", name = "example-py2neo", password='vrwiki81')
graph_search.search_node_name("Tom Hanks")
# a = graph_search.search_node_label("Person")
# print(len(a))
graph_search.search_node_name_label("Person", "Tom Hanks")
graph_search.search_node_label_number("Person", 10)