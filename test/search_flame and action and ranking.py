import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface
from visualization.bar_graph import bar_graph, bar_graph_flame
from query_functions.driver_functions import flame_difference, all_flame_difference_mean
# from py2neo import Graph, 
from neo4j import GraphDatabase

# Neo4jInterfaceはsearchのクラスを引き継いでいる
example = "example-py2neo"
normal = "try"
PASSWORD = 'vrwiki81'
graph = Neo4jInterface("bolt://localhost:7687", name = normal, password=PASSWORD)

"""
ここでやること
KGの全てのobjectに加えられたactionの種類ごとの時間を調べる

"""

label = "Object"

# labelによりそのlabelの全てのノードを検索
# できればここも自動化したいがまあコピペで済む
graph.search_node_label(label)

object_list = ["Slate_Word4", "Booze_Word8", "Persimmon_Word1", "Talisman_Word10", "Canine_Word3", "Snail_Word2", "Crate_Word6", "Pottery_Word5", "Fluff_Word7",  "Fungus_Word9"]
r_type = "bbox"
r_type2 = "next"
target_label = "Bbox"

#今のこれではダメ　一つのObjectにつき一つしかflameが取れない　一つのflameごとにつながっているbboxの数を計算してfor文を回す必要がある
# graph.search_relationship_all_node_flame(label, object_list, r_type, r_type2, target_label)

# python driverを使うやつでいく
# flame_list = flame_difference(label, object_list[0], r_type, r_type2, target_label)
flame_all_dic, flame_dic = all_flame_difference_mean(label, object_list, r_type, r_type2, target_label)

bar_graph(flame_dic, "primitive_action_name", "primitive_action_average_flame")

