# Import the neo4j dependency
from neo4j import GraphDatabase

# Create a new Driver instance
driver = GraphDatabase.driver("neo4j://localhost:7687",
    auth=("neo4j", "neo"))