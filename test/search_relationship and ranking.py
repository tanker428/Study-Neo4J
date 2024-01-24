import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface
from visualization.bar_graph import bar_graph

# Neo4jInterfaceはsearchのクラスを引き継いでいる
example = "example-py2neo"
normal = "try"
graph = Neo4jInterface("bolt://localhost:7687", name = normal, password='vrwiki81')

"""
nodeのランキングを作る

まずはラベルがObjectのノードとmainObjectというリレーションでつながるActionのノードの数を図りランキング化してグラフ化する

グラフの表示方法
このファイルを実行する場合、このファイル上で右クリック
pythonの実行 > ターミナルでpythonを実行を選択
"""


label = "Object"

# labelによりそのlabelの全てのノードを検索
# できればここも自動化したいがまあコピペで済む
graph.search_node_label(label)

object_list = ["Slate_Word4", "Booze_Word8", "Persimmon_Word1", "Talisman_Word10", "Canine_Word3", "Snail_Word2", "Crate_Word6", "Pottery_Word5", "Fluff_Word7",  "Fungus_Word9"]

# objectname = "Pottery_Word5"
relation_name = "mainObject"
target_label = "Action"

# これらの入力からすべてのobject名でactionノードの個数を計算する
score_dict = graph.search_all_relationship_node_number(label, object_list, relation_name, target_label)

# ソートしてグラフ化
# score_sorted_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
bar_graph(score_dict, xlabel="object name", ylabel="number of actions")





# graph.search_relationship_node_number(label, objectname, relation_name, target_label)
# graph.example()



