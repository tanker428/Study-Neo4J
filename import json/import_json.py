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

    jsonの形式
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

    def process_json_data(self, data):
        ___node = self.create_node(data["label_name"], **data['node_information'])

        # Create xxx node and associate it with xxx

        self.create_relationship(__, "HAS_xxx", __)




json_data_open = open('data/sample_data.json', 'r')
json_data = json.load(json_data_open)
print(json_data)


"""
vr-log 

20230829134259 [L] <color=grey>[flame:005044]</color>Event:HoverEnter,By:RHand(Direct),Target:Pottery_Word5]
"""

# Usage
neo4j_interface = Neo4jInterface("bolt://localhost:7687", "try", "vrwiki81")
# my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')

# Assuming you've read your JSON data into a variable called `data`
neo4j_interface.process_json_data(json_data)

