from py2neo import Graph, NodeMatcher

from json_functions.neo4jinterface import Neo4jInterface

# NodeMatcherはどう定義するか分らない
# 公式ページに飛べない
# nodes_matcher = NodeMatcher(graph)
# nodes_matcher.match()

# def search_node():

class SearchAndOverwrite(Neo4jInterface):
    """
    required


    """
    def __init__(self, uri, name, password):
        # self.graph = Graph(uri, name = name, password = password)
        super().__init__(uri, name, password)

#============================================================================
# Node Search

    def search_node_name(self, name: str) -> str:
        """
        property
        nameで探索

        cypher
        MATCH (tom {name: "Tom Hanks"}) RETURN tom
        """

        node_information = self.graph.nodes.match(name = name).first()
        print(f"Node Information: {node_information}")

        return node_information
    
    def search_node_label(self, label: str) -> str:
        node_information = self.graph.nodes.match(label).all()
        print(f"Node Information: {node_information}")

        return node_information

    def search_node_name_label(self, label: str, name: str) -> str:
        """
        property
        name と labelで探索
        """

        node_information = self.graph.nodes.match(label, name = name).first()
        # Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()
        print(f"Node Information: {node_information}")

        return node_information

    """
    これはすべて同じ値
    # keanu = my_graph.nodes.match("Person", name="Keanu Reeves").first()
    # keanu0 = my_graph.nodes[1]
    # keanu1 = my_graph.nodes.get(1)
    """


    """
    titleで探索 title propertyはないので関数作ってない このようにmatchの中に入れれば直接調べられる

    cloud = my_graph.nodes.match(title="Cloud Atlas").first()
    print(f"title_search:{cloud}\n")
    """

    def search_node_label_number(self, label: str, number: int):
        some_node_information = self.graph.nodes.match(label).limit(number).all()
        print(f"{number}個の情報: {some_node_information}")

        return some_node_information
    
    def search_node_label_name_with_query(self, label: str, name: str) -> None:
      query = "Match (node:"+ label +") where node.name = \"" + name + "\" RETURN node"
      node_information = self.graph.evaluate(query)
      print(f"Node Information: {node_information}")

      return node_information
    #============================================================================================
    # node overwrite

    def add_node_property(self, node_information, property_dict: dict) -> None:
        """
        とりあえずdict 1要素のみで対応
        """
        property_key = next(iter(property_dict))
        node_information[property_key] = property_dict[property_key]
        self.graph.push(node_information)
        return

    """
    MATCH (p:Person { name: "Your Name"})
    MATCH (m:Movie { title: "Your Movie"})
    CREATE (p)-[:ACTED_IN]->(m)
    , node_name, destination_node_name, rel: str
    """

    def add_2node_relationship(self) -> None:
        query = "MERGE (p:Person { name: 'Tom Hanks'}) MERGE (m:Person { title: 'Keanu Reeves'}) MERGE (p)-[:ACTED_IN]->(m)"
        self.graph.evaluate(query)
        print("Keanu")

        return
    #==============================================================================================
    # recommend 

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


# recommendに入る
"""
Extend Tom Hanks co-actors, to find co-co-actors who haven't worked with Tom Hanks...

cypher
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors),
      (coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cocoActors)
WHERE NOT (tom)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors) AND tom <> cocoActors
RETURN cocoActors.name AS Recommended, count(*) AS Strength ORDER BY Strength DESC
"""

# results = my_graph.run('MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors), (coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cocoActors) WHERE NOT (tom)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors) AND tom <> cocoActors RETURN cocoActors.name AS Recommended, count(*) AS Strength ORDER BY Strength DESC')
# results = results.data()
# print(f"recommend Tom Hanks co-actor: {results}")

# """
# Find someone to introduce Tom Hanks to Tom Cruise

# cypher
# MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors),
#   (coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cruise:Person {name:"Tom Cruise"})
# RETURN tom, m, coActors, m2, cruise
# """

# results = my_graph.run('MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors), (coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cruise:Person {name:"Tom Cruise"}) RETURN tom, m, coActors, m2, cruise')
# results = results.data()
# print(f"who Tom Hanks and Tom Cruise connection: {results}")