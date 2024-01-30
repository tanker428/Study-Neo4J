import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface
from visualization.bar_graph import bar_graph, bar_graph_flame
from query_functions.driver_functions import flame_difference, all_flame_difference_mean, search_action_and_state_about_object, search_all_action_and_state_about_object
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
graph = Neo4jInterface("bolt://localhost:7687", name = tanakaB, password=PASSWORD)

"""
ここでやること
KGの全てのobjectとつながっているaction名とactionとつながっているslateのbyを検索
できれば動的に表か図を作りたいがめんどいので一旦置いとく
"""

label = "Object"

# labelによりそのlabelの全てのノードを検索
# できればここも自動化したいがまあコピペで済む
graph.search_node_label(label)

object_listA = ["Slate_Word4", "Booze_Word8", "Persimmon_Word1", "Talisman_Word10", "Canine_Word3", "Snail_Word2", "Crate_Word6", "Pottery_Word5", "Fluff_Word7",  "Fungus_Word9"]
object_listB = ["Carving_Word5", "Granite_Word4", "Decor_Word10", "Garland_Word6", "Ewe_Word2", "Dandelion_Word9", "Chick_Word3", "Vintage_Word8", "Acorn_Word1", "Charcoal_Word7"]

object_name = object_listA[0]
object_list = object_listB
r_type = "stateaction"
r_type2 = "mainObject"
target_label = "State"
target_label2 = "Action"
database = tanakaB

# search_action_and_state_about_object(label, object_name, r_type, r_type2, target_label, target_label2, database)
search_all_action_and_state_about_object(label, object_list, r_type, r_type2, target_label, target_label2, database)