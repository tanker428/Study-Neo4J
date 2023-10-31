from py2neo import Graph, RelationshipMatcher, NodeMatcher

my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')

"""
Delete all Movie and Person nodes, and their relationships

cypher
MATCH (n) DETACH DELETE n
"""

number = len(my_graph.match())
print(f"before mygraph node: {number}")

# my_graph.delete_all()

number = len(my_graph.match())
print(f"after mygraph node: {number}")
