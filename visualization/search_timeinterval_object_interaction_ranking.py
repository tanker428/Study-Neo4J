import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface
from visualization.bar_graph import bar_graph, bar_graph_flametime
from query_functions.driver_functions import flame_difference, all_flame_difference_mean
# from py2neo import Graph, 
from neo4j import GraphDatabasea

# Neo4jInterfaceはsearchのクラスを引き継いでいる
example = "example-py2neo"
normal = "try"
nishiA = "nishiAver2"
nishiB = "nishiBver2"
tanakaA = "tanakaAver2"
tanakaB = "tanakaBver2"
PASSWORD = 'vrwiki81'


name = tanakaB

graph = Neo4jInterface("bolt://localhost:7687", name = name, password=PASSWORD)

"""
ここでやること
KGの全てのobjectに加えられたactionの種類ごとのインタラクション数をシナリオで時間を区切って行う
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


# python driverを用いる
flame_all_dic, flame_dic = all_flame_difference_mean(label, object_listB, r_type, r_type2, target_label, name)

# bar_graph(flame_dic, "primitive_action_name", "primitive_action_average_flame")

# flame_all_dic = {'Slate': {'size': 52, 'sum': 6911.0, 'mean': 132.90384615384616}, 'Booze': {'size': 41, 'sum': 4308.0, 'mean': 105.07317073170732}, 'Persimmon_Word1': {'size': 26, 'sum': 4980.0, 'mean': 191.53846153846155}, 'Talisman_Word10': {'size': 12, 'sum': 3096.0, 'mean': 258.0}, 'Canine_Word3': {'size': 26, 'sum': 4616.0, 'mean': 177.53846153846155}, 'Snail_Word2': {'size': 31, 'sum': 3356.0, 'mean': 108.25806451612904}, 'Crate_Word6': {'size': 17, 'sum': 2318.0, 'mean': 136.35294117647058}, 'Pottery_Word5': {'size': 46, 'sum': 5769.0, 'mean': 125.41304347826087}, 'Fluff_Word7': {'size': 11, 'sum': 2592.0, 'mean': 235.63636363636363}, 'Fungus_Word9': {'size': 46, 'sum': 4816.0, 'mean': 104.69565217391305}}

bar_graph_flametime(flame_all_dic, "primitive_action_name", "primitive_action_average_flame")