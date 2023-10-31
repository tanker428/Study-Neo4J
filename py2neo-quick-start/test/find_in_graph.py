from py2neo import Graph, NodeMatcher

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

cypher
MATCH (tom {name: "Tom Hanks"}) RETURN tom
"""

Tom = my_graph.nodes.match(name="Tom Hanks").first()
Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()


print(f"Tom node information:{Tom}\n")
print(f"Person Tom node information:{Person_Tom}\n")



keanu = my_graph.nodes.match("Person", name="Keanu Reeves").first()
keanu0 = my_graph.nodes[1]
keanu1 = my_graph.nodes.get(1)


print(f"name_search:{keanu0 == keanu1 == keanu}\n")

"""
titleで探索
"""

cloud = my_graph.nodes.match(title="Cloud Atlas").first()

print(f"title_search:{cloud}\n")

"""
nodeのlabelでの個数
"""

person_amount = len(my_graph.nodes.match("Person"))

print(f"person人数:{person_amount}\n")


"""
find 10 node of "person"

cypher
MATCH (people:Person) RETURN people.name LIMIT 10
"""

ten_person = my_graph.nodes.match("Person").limit(10).all()
print(f"10人: {ten_person}\n")

"""
find node of "movies" property of "released"

cypher
MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title
飛ばす
"""

# whereの使い方が分らん
# movies_1990 = my_graph.nodes.match("Movies", released="1995").first()
# print(f"1990movies: {movies_1990}\n")
# print(movies_1990.count())

