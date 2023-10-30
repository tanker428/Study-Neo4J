from py2neo import Graph, RelationshipMatcher, NodeMatcher
from py2neo.integration import Table
import pandas, sympy, numpy

my_graph = Graph("bolt://localhost:7687", name = "try", password='vrwiki81')
# my_graph.nodes.match()

"""
relationship
"""

matcher = NodeMatcher(my_graph)

relationship_matcher = RelationshipMatcher(my_graph)
relationship_matcher.match()

my_graph.relationships.match()

"""
list all Tom Hanks movies

cypher
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies
"""

Tom = my_graph.nodes.match(name="Tom Hanks").first()
Toms = my_graph.match(nodes=[Tom], r_type="ACTED_IN").all()
print(f"Tom Hanks acted in movies: {Toms}\n")

"""
who directed "Cloud Atlas"? 

cypher
MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name

a pattern
"""

results = my_graph.run('MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name')
results = results.data()

print(f"Cloud Atlas actors: {results}\n")

"""
b pattern
"""
cloudAtlas = matcher.match(title="Cloud Atlas").first()
directors = my_graph.match(r_type="DIRECTED", nodes=(None, cloudAtlas)) # << see notes about use of nodes=() here
for director in directors:
     print(director.nodes[0]['name'])
print("\n")


"""
Tom Hanks' co-actors

cypher
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name
"""

results = my_graph.run('MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name')
results = results.data()
print(f"Tom Hanks' co-actors: {results}\n")

"""
How people are related to "Cloud Atlas"

cypher
MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo
"""

results = my_graph.run('MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo')
result = results.data()
print(f"how related 'Cloud Atlas': {result}\n")

# 分ければいける
query_string = 'MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo'
results_table = my_graph.run(query_string).to_table()
print(f"table出力: {results_table}\n")

# pythonを用いて出力をいじれる 元
results = my_graph.run(query_string)

# pandas
result_data_frame = results.to_data_frame()
print(f"pandas data_frame: {result_data_frame}\n")

result_series = results.to_series()
print(f"pandas series: {result_series}\n")

# sympy
result_matrix = results.to_matrix()
print(f"sympy matrix: {result_matrix}\n")

# numpy
result_ndarray = results.to_ndarray()
print(f"numpy ndaaray: {result_ndarray}\n")