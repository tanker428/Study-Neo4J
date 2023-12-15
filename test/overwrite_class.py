import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from query_functions.query_functions import SearchAndOverwrite

graph = SearchAndOverwrite("bolt://localhost:7687", name = "try", password='vrwiki81')

add_rel = graph.search_node_name_label("User", "nishi")