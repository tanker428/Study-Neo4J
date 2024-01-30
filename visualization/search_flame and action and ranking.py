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
nishiA = "nishiAver2"
nishiB = "nishiBver2"
tanakaA = "tanakaAver2"
tanakaB = "tanakaBver2"
PASSWORD = 'vrwiki81'
graph = Neo4jInterface("bolt://localhost:7687", name = tanakaA, password=PASSWORD)

"""
ここでやること
KGの全てのobjectに加えられたactionの種類ごとの時間を調べる

"""

label = "Object"

# labelによりそのlabelの全てのノードを検索
# できればここも自動化したいがまあコピペで済む
graph.search_node_label(label)

object_listA = ["Slate_Word4", "Booze_Word8", "Persimmon_Word1", "Talisman_Word10", "Canine_Word3", "Snail_Word2", "Crate_Word6", "Pottery_Word5", "Fluff_Word7",  "Fungus_Word9"]
object_listB = ["Carving_Word5", "Granite_Word4", "Decor_Word10", "Garland_Word6", "Ewe_Word2", "Dandelion_Word9", "Chick_Word3", "Vintage_Word8", "Acorn_Word1", "Charcoal_Word7"]
r_type = "bbox"
r_type2 = "next"
target_label = "Bbox"

#今のこれではダメ　一つのObjectにつき一つしかflameが取れない　一つのflameごとにつながっているbboxの数を計算してfor文を回す必要がある
# graph.search_relationship_all_node_flame(label, object_list, r_type, r_type2, target_label)

# python driverを使うやつでいく
# flame_list = flame_difference(label, object_list[0], r_type, r_type2, target_label)
flame_all_dic, flame_dic = all_flame_difference_mean(label, object_listA, r_type, r_type2, target_label, tanakaA)

# flame_dic_nishiB = {'Carving': 186.83333333333334, 'Granite': 190.04166666666666, 'Decor': 0, 'Garland': 279.94736842105266, 'Ewe': 171.09803921568627, 'Dandelion': 464.3333333333333, 'Chick': 187.0, 'Vintage': 321.75, 'Acorn': 50.705882352941174, 'Charcoal': 429.0} 
# flame_dic_tanakaB = {'Carving': 143.4, 'Granite': 314.22222222222223, 'Decor': 154.2, 'Garland': 51.8421052631579, 'Ewe': 91.0, 'Dandelion': 226.33333333333334, 'Chick': 148.61818181818182, 'Vintage': 308.0, 'Acorn': 56.8433734939759, 'Charcoal': 188.32}
flame_dic ={'Slate': 132.90384615384616, 'Booze': 208.74074074074073, 'Persimmon': 183.3448275862069, 'Talisman': 243.2, 'Canine': 173.58620689655172, 'Snail': 107.74285714285715, 'Crate': 136.0, 'Pottery': 114.19298245614036, 'Fluff': 302.11764705882354, 'Fungus': 907.4}
bar_graph(flame_dic, "primitive_action_name", "primitive_action_average_flame")

