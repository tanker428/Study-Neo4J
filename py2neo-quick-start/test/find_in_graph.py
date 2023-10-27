from py2neo import Graph

my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')
my_graph.nodes.match()

# NodeMatcherはどう定義するか分らない
# 公式ページに飛べない
# nodes_matcher = NodeMatcher(graph)
# nodes_matcher.match()

"""
node探索

property
nameで探索
titleで探索
"""

keanu = my_graph.nodes.match("Person", name="Keanu Reeves").first()
print(f"name:{keanu}")

keanu0 = my_graph.nodes[1]
keanu1 = my_graph.nodes.get(1)


print(f"name_search:{keanu0 == keanu1 == keanu}")

cloud = my_graph.nodes.match(title="Cloud Atlas").first()

print(f"title_search:{cloud}")

"""
nodeのlabelでの個数
"""

person_amount = len(my_graph.nodes.match("Person"))

print(f"person人数:{person_amount}")


