import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver=GraphDatabase.driver(NEO4J_URI,auth=(NEO4J_USERNAME,NEO4J_PASSWORD))

def verify_connection():
    try:
        driver.verify_connectivity()
        print("Neo4j connected successfully")
    except Exception  as e:
        print("Neo4j connection failed")
        print(e)
    finally:
        driver.close()

if __name__=="__main__":
    verify_connection()
