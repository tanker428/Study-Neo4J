from py2neo import Graph, Node, Relationship
import json
# import os
# import sys
# import math
# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# from data import 


class Neo4jInterface:
    """
    required
        uri: dbのuri
        user: dbのname
        passward: dbのpassword

    jsonの形式 だんだん変わってる
        json = 
        {
            "label_name":
                {
                    "property_name": "content",
                    ...
                }
        }

    """
    def __init__(self, uri, user, password):
        self.graph = Graph("bolt://localhost:7687", name = user, password = password)

    def create_node(self, label, **properties):
        node = Node(label, **properties)
        self.graph.create(node)
        return node

    def create_relationship(self, node1, relationship_type, node2, **properties):
        rel = Relationship(node1, relationship_type, node2, **properties)
        self.graph.create(rel)


    def create_3node(self, json_data: dict) -> dict:
        """
        node作成 labelデータを制作
        """
        
        data1 = json_data["node_1"]
        data2 = json_data["node_2"]
        data3 = json_data["node_3"]

        node1 = self.create_node(data1["label_name"], **data1['node_information'])
        node2 = self.create_node(data2["label_name"], **data2['node_information'])
        node3 = self.create_node(data3["label_name"], **data3['node_information'])

        label_name1 = data1["label_name"]
        label_name2 = data2["label_name"]
        label_name3 = data3["label_name"]

        node_dict = {"node1": node1, "node2": node2, "node3": node3,
                     "label1": label_name1, "label2": label_name2, "label3": label_name3}

        return node_dict

    def create_3node_2relation(self, node_dict: dict) -> None:
        """
        3nodeを2relationでつなぐ
        方向はdata1 -> data2
        """

        # node
        node1 = node_dict["node1"]
        node2 = node_dict["node2"]
        node3 = node_dict["node3"]

        # relation7
        rel1 = f'{node_dict["label1"]}_{node_dict["label2"]}'
        rel2 = f'{node_dict["label2"]}_{node_dict["label3"]}'

        self.create_relationship(node1, rel1, node2)
        self.create_relationship(node2, rel2, node3)

    def json_to_3node_graph(self, json_path: str) -> None:
        """
        jsonから目的語,助詞,動詞のグラフを作成
        """
        # data整理
        json_data_open = open(json_path, 'r', encoding="utf-8")
        json_data = json.load(json_data_open)
        print(f"json_data: {json_data}")

        # ノード化
        node_dict = self.create_3node(json_data)

        # リレーション化
        self.create_3node_2relation(node_dict)
        

    def create_5node(self, json_data: dict) -> dict:
        """
        5nodeを4relationでつなぐ
        方向はdata1 -> data2...
        """
        
        data1 = json_data["node_1"]
        data2 = json_data["node_2"]
        data3 = json_data["node_3"]
        data4 = json_data["node_4"]
        data5 = json_data["node_5"]

        node1 = self.create_node(data1["label_name"], **data1['node_information'])
        node2 = self.create_node(data2["label_name"], **data2['node_information'])
        node3 = self.create_node(data3["label_name"], **data3['node_information'])
        node4 = self.create_node(data4["label_name"], **data4['node_information'])
        node5 = self.create_node(data5["label_name"], **data5['node_information'])

        label_name1 = data1["label_name"]
        label_name2 = data2["label_name"]
        label_name3 = data3["label_name"]
        label_name4 = data4["label_name"]
        label_name5 = data5["label_name"]

        node_dict = {"node1": node1, "node2": node2, "node3": node3, "node4": node4, "node5": node4,
                     "node5": node5, "label1": label_name1, "label2": label_name2, "label3": label_name3,
                     "label4": label_name4, "label5": label_name5}

        return node_dict

    def create_5node_4relation(self, node_dict: dict) -> None:

        # node
        node1 = node_dict["node1"]
        node2 = node_dict["node2"]
        node3 = node_dict["node3"]
        node4 = node_dict["node4"]
        node5 = node_dict["node5"]

        # relation
        rel1 = f'{node_dict["label1"]}_{node_dict["label2"]}'
        rel2 = f'{node_dict["label2"]}_{node_dict["label3"]}'
        rel3 = f'{node_dict["label3"]}_{node_dict["label4"]}'
        rel4 = f'{node_dict["label4"]}_{node_dict["label5"]}'

        self.create_relationship(node1, rel1, node2)
        self.create_relationship(node2, rel2, node3)
        self.create_relationship(node3, rel3, node4)
        self.create_relationship(node4, rel4, node5)

    def create_graph(self, node_data: dict) -> None:
        """
        node数に応じてどうrelationを作成するか
        """
        node_data_size = len(node_data)
        print(f"node数: {node_data_size}")
        if node_data_size == 3:
             # ノード化
            node_dict = self.create_3node(node_data)

            # リレーション化
            self.create_3node_2relation(node_dict)

        elif node_data_size == 5:
             # ノード化
            node_dict = self.create_5node(node_data)

            # リレーション化
            self.create_5node_4relation(node_dict)
            


    def json_to_allnode_graph(self, json_path: str) -> None:
        """
        リスト内の全てのnodeをグラフ化する
        """
        # data整理
        json_data_open = open(json_path, 'r', encoding="utf-8")
        json_data = json.load(json_data_open)
        print(f"json_data: {json_data}")

        for n in range(len(json_data)):
            relation_data = json_data[n]
            self.create_graph(relation_data)

    def delete_all_node(self) -> None:
        """
        データベースの全てのノードを削除する
        """
        self.graph.delete_all()



"""
vr-log 

20230829134259 [L] <color=grey>[flame:005044]</color>Event:HoverEnter,By:RHand(Direct),Target:Pottery_Word5]
"""

# Usage
# neo4j_interface = Neo4jInterface("bolt://localhost:7687", "try", "vrwiki81")
# my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')

# Assuming you've read your JSON data into a variable called `data`
# neo4j_interface.process_json_data(json_data)

