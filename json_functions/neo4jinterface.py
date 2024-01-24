from py2neo import Graph, Node, Relationship
import json
import os
import sys
import math
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from query_functions.query_functions import SearchAndOverwrite 


class Neo4jInterface(SearchAndOverwrite):
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
    """
    基本関数
    """
    def __init__(self, uri, name, password):
        super().__init__(uri, name, password)
        # self.before_flame = None
        # self.graph = Graph(uri, name = name, password = password)

    def set_before_flame(self):
        self.before_flame = "-1"
        self.before_timestamp = "-1"

    def create_node(self, label, **properties):
        node = Node(label, **properties)
        self.graph.create(node)
        return node

    def create_relationship(self, node1, relationship_type, node2, **properties):
        """
        node1 -> node2 
        """
        rel = Relationship(node1, relationship_type, node2, **properties)
        self.graph.create(rel)

    """
    自作関数
    """
    def create_1node(self, json_data: dict) -> dict:
        """
        1ノード作成 relationはなし
        """

        key = next(iter(json_data))
        data1 = json_data[key]
        # print(f"key: {key}\n")
        # print(f"data1: {data1}\n")
        user_name = data1["node_information"]["username"]

        # User nodeデータもここで作成する
        data2 = {
            "label_name": "User", "node_information": {
                "name" : user_name
            }
        }

        # nodeが既に存在するかどうかをチェック
        label1 = data1["label_name"]
        name1 = data1["node_information"]["name"]
        flame1 = data1["node_information"]["flame"]

        label2 = data2["label_name"]
        name2 = user_name

        exist_node1 = self.check_if_node_exist_flame(label1, name1, flame1)
        exist_node2 = self.check_if_node_exist(label2, name2)

        # 過去にnodeがぞんざいしない
        if exist_node1 == None:
            node1 = self.create_node(data1["label_name"], **data1['node_information'])

            if exist_node2 == None:
                node2 = self.create_node(data2["label_name"], **data2["node_information"])
                exist_node = 0 

            else:
                node2 = exist_node2
                exist_node = 1
        else:
            node1 = exist_node1
            if exist_node2 == None:
                node2 = self.create_node(data2["label_name"], **data2["node_information"])
                exist_node = 2

            else:
                node2 = exist_node2
                exist_node = 3

        
        # print(user_name)
        node_dict = {"node1": node1, "node2": node2, "label1": user_name, "exist_node": exist_node}
        return node_dict
    
    def create_node_ontology_ver2(self, json_data: dict) -> dict:
        """
        ontology ver2の構造を作成する

        一回のlogで
        User   : timestamp
            state
        State  : flame by
            action 
        Action : actionname event 
            mainObject
        Object : name
            bbox
        Bbox   : timestamp flame
        """
        

        json_key = next(iter(json_data))
        data_sum = json_data[json_key]
        data_sum_inf = data_sum["node_information"]
        # print(f"key: {key}\n")
        # print(f"data1: {data1}\n")

        user_name = data_sum_inf["username"]
        flame = data_sum_inf["flame"]
        by = data_sum_inf["by"]
        event = data_sum_inf["event"]
        name = data_sum_inf["name"]
        timestamp = data_sum_inf["timestamp"]

        # action_name
        if event == "HoverEnter":
            action_name = "触れる"
        elif event == "HoverExit":
            action_name = "離れる"
        elif event == "SelectEnter":
            action_name = "つかむ"
        elif event == "SelectExit" :
            action_name = "離す"
        else:
            action_name = "不明"

        ## node データの成型
        # User 

        data_user = {
            "label_name": "User", "node_information": {
                "username" : user_name
            }
        }

        # State

        data_state = {
            "label_name" : "State", "node_information": {
                "flame" : flame, "by" : by
            }
        }

        # Action

        data_action = {
            "label_name" : "Action", "node_information": {
                "event" : event, "actionname" : action_name
            }
        }

        # Object

        data_object = {
            "label_name" : "Object", "node_information": {
                "objectname" : name
            }
        }

        # Bbox
        data_bbox = {
            "label_name" : "Bbox", "node_information": {
                "timestamp" : timestamp, "flame" : flame,
                "event" : event
            }
        }
        
        ## Relation
        # user -> state
        label_userstate = "state"

        # state -> action
        label_stateaction = "stateaction"

        # action -> object
        label_actionobject = "mainObject"

        # object -> bbox
        label_objectbbox = "bbox"

        # nodeを常に新しく生成
        node_state = self.create_node(data_state["label_name"], **data_state["node_information"])
        node_action = self.create_node(data_action["label_name"], **data_action["node_information"])
        node_bbox = self.create_node(data_bbox["label_name"], **data_bbox["node_information"])


        # nodeが既に存在するかどうかをチェック
        label_user = data_user["label_name"]
        label_object = data_object["label_name"]
        label_bbox = data_bbox["label_name"]

        exist_object = self.check_if_object_exist(label_object, name)
        exist_user = self.check_if_user_exist(label_user, user_name)

       
        
        # if self.before_flame == None:
        #     exist_bbox = None
        #     self.before_flame = flame

        #     print(f"before flame: {self.before_flame}")
        #     print(f"flame: {flame}")
        # else:
        exist_bbox = self.check_if_node_exist_flame_timestamp(label_bbox, self.before_flame, self.before_timestamp)
            
        print(f"before flame: {self.before_flame}")
        print(f"flame: {flame}")
        
        # exist_object = None
        # exist_user = None

        # 過去にnodeがぞんざいしない
        if exist_user == None:
            node_user = self.create_node(data_user["label_name"], **data_user['node_information'])

            if exist_object == None:
                node_object = self.create_node(data_object["label_name"], **data_object["node_information"])
                exist_node = "new user & new object"

            else:
                node_object = exist_object
                exist_node = "new user & exist object"
        else:
            node_user = exist_user
            if exist_object == None:
                node_object = self.create_node(data_object["label_name"], **data_object["node_information"])
                exist_node = "exist user & new object"

            else:
                node_object = exist_object
                exist_node = "exist user & exist object"
        
        if exist_bbox == None:
            node_before_bbox = None
            print("bbox none") 
        else:
            node_before_bbox = exist_bbox
        self.before_flame = flame
        self.before_timestamp = timestamp
        
        print(f"about node: {exist_node}")
        node_dict = {"node_user": node_user, "node_state": node_state, "node_action": node_action,
                     "node_object": node_object, "node_bbox": node_bbox, "node_before_bbox": node_before_bbox,
                     "label_userstate": label_userstate, "label_stateaction": label_stateaction, 
                     "label_actionobject": label_actionobject, "label_objectbbox": label_objectbbox,
                     }
        return node_dict

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

    def create_user_object_relation(self, node_dict: dict) -> None:
        # 問題点　user nodeデータ 保管　propertyに入れてその情報を参照してuser名を入れる

        node1 = node_dict["node1"]
        rel1 = node_dict["label1"]
        node2 = node_dict["node2"]
        
        exist_node = node_dict["exist_node"]
        print(f"exist_node: {exist_node}")

        self.create_relationship(node1, rel1, node2)
        return
    
    def create_relation_ontology_ver2(self, node_dict: dict) -> None:
        
        # User -> State
        node1 = node_dict["node_user"]
        rel1 = node_dict["label_userstate"]
        node2 = node_dict["node_state"]
        self.create_relationship(node1, rel1, node2)


        # State -> Action
        node1 = node_dict["node_state"]
        rel1 = node_dict["label_stateaction"]
        node2 = node_dict["node_action"]
        self.create_relationship(node1, rel1, node2)

        # Action -> Object
        node1 = node_dict["node_action"]
        rel1 = node_dict["label_actionobject"]
        node2 = node_dict["node_object"]
        self.create_relationship(node1, rel1, node2)

        # Object -> Bbox
        node1 = node_dict["node_object"]
        rel1 = node_dict["label_objectbbox"]
        node2 = node_dict["node_bbox"]
        self.create_relationship(node1, rel1, node2)

        # before BBox -> after BBox
        node1 = node_dict["node_before_bbox"]
        if node1 == None:
            pass

        else:
            rel1 = "next"
            node2 = node_dict["node_bbox"]
            self.create_relationship(node1, rel1, node2)

        return

    def json_to_3node_graph(self, json_path: str) -> None:
        """
        jsonから目的語,助詞,動詞のグラフを作成
        多分, json_to_all_nodeが上位互換
        """
        # data整理
        json_data_open = open(json_path, 'r', encoding="utf-8")
        json_data = json.load(json_data_open)
        print(f"json_data: {json_data}")

        # ノード化
        node_dict = self.create_3node(json_data)

        # リレーション化
        self.create_3node_2relation(node_dict)

    def create_graph(self, node_data: dict, ontology_number: int) -> None:
        """
        node数に応じてどうrelationを作成するか

        nodeがあるかどうかをまず検索する
        ないなら作る あるなら上書きする方針
        """
        node_data_size = len(node_data)
        print(f"node数: {node_data_size}")
        if node_data_size == 3 and ontology_number == 0:
            print("3node_2relation")
             # ノード化
            node_dict = self.create_3node(node_data)

            # リレーション化
            self.create_3node_2relation(node_dict)

        elif node_data_size == 5 and ontology_number == 0:
            print("5node_4relation")
             # ノード化
            node_dict = self.create_5node(node_data)

            # リレーション化
            self.create_5node_4relation(node_dict)

        elif node_data_size == 1 and ontology_number == 1:
            print("ontology1")
            # ノード化のみ
            node_dict = self.create_1node(node_data)

            # リレーション化
            self.create_user_object_relation(node_dict)

        elif node_data_size == 1 and ontology_number == 2:
            print("ontology2")
            # ノード化のみ
            node_dict = self.create_node_ontology_ver2(node_data)

            # リレーション化
            self.create_relation_ontology_ver2(node_dict)


    def json_to_allnode_graph(self, json_path: str, ontology_number: int) -> None:
        """
        リスト内の全てのnodeをグラフ化する

        ontology_number 
            number = 0 初期のデータ 
            3, 5でnodeとrelationを作成

            number = 1 第一オントロジーデータ
            userとobjectのみで作成
        """
        # data整理
        json_data_open = open(json_path, 'r', encoding="utf-8")
        json_data = json.load(json_data_open)
        print(f"json_data: {json_data}")

        for n in range(len(json_data)):
            relation_data = json_data[n]
            self.create_graph(relation_data, ontology_number)

    def delete_all_node(self) -> None:
        """
        データベースの全てのノードを削除する
        """
        self.graph.delete_all()


"""        # super().__init__(uri, name, password)

vr-log 
20230829134259 [L] <color=grey>[flame:005044]</color>Event:HoverEnter,By:RHand(Direct),Target:Pottery_Word5]

使っていない関数

・直接データを入れてNode作成
CastAway = Node("Movie", title='Cast Away', released=2000,
                tagline='At the edge of the world, his journey begins.')

・直接データを入れてRelation作成
AaronSAFewGoodMen = Relationship(AaronS, "WROTE", AFewGoodMen)

・後付けでNodeデータを入れる
CarrieTheMatrix['roles'] = ['Trinity']

・静的にNodeを生成する
tx = my_graph.begin()
tx.create(AFewGoodMen)
tx.commit()          
"""



