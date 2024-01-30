import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from json_functions.neo4jinterface import Neo4jInterface
from visualization.bar_graph import bar_graph

# Neo4jInterfaceはsearchのクラスを引き継いでいる
example = "example-py2neo"
normal = "try"
nishiA = "nishiAver2"
nishiB = "nishiBver2"
tanakaA = "tanakaAver2"
tanakaB = "tanakaBver2"
graph = Neo4jInterface("bolt://localhost:7687", name = tanakaA, password='vrwiki81')

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

object_listA = ["Slate_Word4", "Booze_Word8", "Persimmon_Word1", "Talisman_Word10", "Canine_Word3", "Snail_Word2", "Crate_Word6", "Pottery_Word5", "Fluff_Word7",  "Fungus_Word9"]
object_listB = ["Carving_Word5", "Granite_Word4", "Decor_Word10", "Garland_Word6", "Ewe_Word2", "Dandelion_Word9", "Chick_Word3", "Vintage_Word8", "Acorn_Word1", "Charcoal_Word7"]

# objectname = "Pottery_Word5"
relation_name = "mainObject"
target_label = "Action"

# これらの入力からすべてのobject名でactionノードの個数を計算する
score_dict = graph.search_all_relationship_node_number(label, object_listA, relation_name, target_label)
print(score_dict)
"""
ここまでで一旦出力してscore_dictをべた張りする
_word1とかを取り除くため
"""

# score_dict_nishiB = {'Carving': 31, 'Granite': 25, 'Decor': 0, 'Garland': 19, 'Ewe': 55, 'Dandelion': 3, 'Chick': 35, 'Vintage': 16, 'Acorn': 27, 'Charcoal': 15}
# score_dict_tanakaB = {'Carving': 61, 'Granite': 19, 'Decor': 30, 'Garland': 39, 'Ewe': 76, 'Dandelion': 6, 'Chick': 56, 'Vintage': 10, 'Acorn': 75, 'Charcoal': 23}
score_dict = {'Slate': 52, 'Booze': 27, 'Persimmon': 26, 'Talisman': 15, 'Canine': 32, 'Snail': 35, 'Crate': 21, 'Pottery': 56, 'Fluff': 18, 'Fungus': 5}
# ソートしてグラフ化
# score_sorted_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
bar_graph(score_dict, xlabel="object name", ylabel="number of actions")





# graph.search_relationship_node_number(label, objectname, relation_name, target_label)
# graph.example()



