from py2neo import Graph, RelationshipMatcher, NodeMatcher

my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')

"""
solve

You've heard of the classic "Six Degrees of Kevin Bacon"? That is simply a shortest path query called the "Bacon Path".

Variable length patterns
Built-in shortestPath() algorithm
"""


"""
Movies and actors up to 4 "hops" away from Kevin Bacon

cypher
MATCH (bacon:Person {name:"Kevin Bacon"})-[*1..4]-(hollywood)
RETURN DISTINCT hollywood
"""

results = my_graph.run('MATCH (bacon:Person {name:"Kevin Bacon"})-[*1..4]-(hollywood) RETURN DISTINCT hollywood')
results = results.data()
number = len(results)

print(f"node hops: {results, number}\n")

"""
Bacon path, the shortest path of any relationships to Meg Ryan

cypher
MATCH p=shortestPath(
  (bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})
)
RETURN p
"""

results = my_graph.run('MATCH p=shortestPath((bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})) RETURN p')
results = results.data()

print(f"shortest path Kevin Beacon, Meg Ryan: {results}\n")
