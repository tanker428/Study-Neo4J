from py2neo import Graph, NodeMatcher

# from json_functions.neo4jinterface import Neo4jInterface

# NodeMatcherはどう定義するか分らない
# 公式ページに飛べない
# nodes_matcher = NodeMatcher(graph)
# nodes_matcher.match()

# def search_node():

class SearchAndOverwrite():
    """
    required


    """
    def __init__(self, uri, name, password):
        self.graph = Graph(uri, name = name, password = password)
        # super().__init__(uri, name, password)

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
        print(f"check Node Information: {node_information}")

        return node_information
    
    def search_node_name_label_flame(self, label: str, name: str, flame: str) -> str:
        """
        property
        name と labelで探索
        """

        node_information = self.graph.nodes.match(label, name = name, flame=flame).first()
        # Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()
        print(f"check_flame Node Information: {node_information}")

        return node_information
    
    def search_node_flame_timestamp(self, label: str, flame: str, timestamp: str):
        node_information = self.graph.nodes.match(label, flame = flame, timestamp=timestamp).first()
        # Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()
        print(f"check_flame Node Information: {node_information}")        

        return node_information

    def search_node_username_label(self, label: str, username: str) -> str:
        """
        property
        usernameでUser探索
        """

        node_information = self.graph.nodes.match(label, username = username).first()
        # Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()
        print(f"check User Information: {node_information}")

        return node_information
    
    def search_node_objectname_label(self, label: str, objectname: str) -> str:
        """
        property
        objectnameでUser探索
        """

        node_information = self.graph.nodes.match(label, objectname = objectname).first()
        # Person_Tom = my_graph.nodes.match("Person", name="Tom Hanks").first()
        print(f"check Object Information: {node_information}")
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
      print(f"check Node Information: {node_information}")

      return node_information
    
    def search_node_label_username_with_query(self, label: str, name: str) -> None:
      query = "Match (node:"+ label +") where node.username = \"" + name + "\" RETURN node"
      node_information = self.graph.evaluate(query)
      print(f"check User Information: {node_information}")

      return node_information
    
    def search_node_label_object_with_query(self, label: str, name: str) -> None:
      query = "Match (node:"+ label +") where node.objectname = \"" + name + "\" RETURN node"
      node_information = self.graph.evaluate(query)
      print(f"check Object Information: {node_information}")

      return node_information
    
    def search_node_label_name_flame_with_query(self, label: str, name: str, flame: str) -> None:
      query = "Match (node:"+ label +") where node.name = \"" + name + "\" AND node.flame = \" "+ flame +" \" RETURN node"
      node_information = self.graph.evaluate(query)
      print(f"check Node Information: {node_information}")

      return node_information
    
    def search_node_label_flame_timestamp_with_query(self, label: str, flame: str, timestamp: str) -> None:
      query = "Match (node:"+ label +") where node.flame = \"" + flame + "\" AND node.timestamp = \" "+ timestamp +" \" RETURN node"
      node_information = self.graph.evaluate(query)
      print(f"check flame timestamp Node Information: {node_information}")

      return node_information
    
    #==============================================================================================

    def search_relationship(self, node, r_type: str) -> None:
        """
        nodeが変数として入力された場合にそのnodeの指定したrelationを全て取り出す
        できないのでquery直接ぶち込みをやる
        """
        label = "Object"
        Pot = self.graph.nodes.match(label, name="Pottery_Word5").first()
        node_relation = self.graph.relationships.match(nodes=[Pot], r_type="mainObject").all()
        node_relation_number = len(node_relation)
        print(f"relation imformation: {node_relation}")

        # query = 'Match (obj:Object)-[r:mainObject]-(act:Action) where obj.objectname="Pottery_Word5" return act'
        query = 'Match (obj:Object)-[r:mainObject]-(act:Action) where obj.objectname="Pottery_Word5" return count(act) as action_count'
        node_information = self.graph.evaluate(query)
        
        print(f"relation number: {node_information}")

        # query = "Match (node:"+ label +") where node.name = \"" + name + "\" AND node.flame = \" "+ flame +" \" RETURN node"
        # node_information = self.graph.evaluate(query)
        return
    
    # Tom = my_graph.nodes.match(name="Tom Hanks").first()
    # Toms = my_graph.match(nodes=[Tom], r_type="ACTED_IN").all()
    # print(f"Tom Hanks acted in movies: {Toms}\n")

    def example(self):
        Tom = self.graph.nodes.match(name="Tom Hanks").first()
        Toms = self.graph.relationships.match(nodes=[Tom], r_type="ACTED_IN").all()
        tom_number = len(Toms)
        print(f"Tom Hanks acted in movies: {Toms}\n")
        print(f"tom number: {tom_number}")
        query = 'MATCH (p:Person {name: "Tom Hanks"})-[:ACTED_IN]->(m:Movie) RETURN m'
        node_information = self.graph.evaluate(query)
        print(node_information)
        return
    #==============================================================================================
    
    def check_if_node_exist(self, label: str, name: str):
        """
        過去に同じnodeがなかったかどうかをチェックする
        """
        node_exist = self.search_node_name_label(label, name)
        if node_exist == None:
            node_exist == self.search_node_label_name_with_query(label, name)

        return node_exist
    
    def check_if_user_exist(self, label: str, username: str):
        """
        過去に同じnodeがなかったかどうかをチェックする
        """
        node_exist = self.search_node_username_label(label, username)
        if node_exist == None:
            node_exist == self.search_node_label_username_with_query(label, username)

        return node_exist
    
    def check_if_object_exist(self, label: str, objectname: str):
        """
        過去に同じnodeがなかったかどうかをチェックする
        """
        node_exist = self.search_node_objectname_label(label, objectname)
        if node_exist == None:
            node_exist == self.search_node_label_object_with_query(label, objectname)

        return node_exist
    
    def check_if_node_exist_flame(self, label: str, name: str, flame: str):
        """
        過去に同じnodeがなかったかどうかをチェックする
        """
        node_exist = self.search_node_name_label_flame(label, name, flame)
        if node_exist == None:
            node_exist == self.search_node_label_name_flame_with_query(label, name, flame)

        return node_exist
    
    def check_if_node_exist_flame_timestamp(self, label: str, flame: str, timestamp: str):
        """
        過去に同じnodeがなかったかどうかをチェックする
        """
        node_exist = self.search_node_flame_timestamp(label, flame, timestamp)
        if node_exist == None:
            node_exist == self.search_node_label_flame_timestamp_with_query(label, flame, timestamp)

        return node_exist
    
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

    def old_node_relationship(self, node_name: str, destination_name: str, rel: str):
       """
       既にあるnode同士に新しいrelationを加える
       """
       query = "MERGE (p:Person { name: '" + node_name + "'}) MERGE (m:Person { name: '" + destination_name + "'}) MERGE (p)-[:" + rel + "]->(m)"
       self.graph.evaluate(query)
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
