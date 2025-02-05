from neo4j import GraphDatabase

def get_db_connection():
    # Set up your Neo4j connection
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "password"
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver
