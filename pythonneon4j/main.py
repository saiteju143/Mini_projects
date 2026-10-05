
from neon4jconnection import driver


def create_test_node():
    try:
        print("Connecting to Neo4j...")

        with driver.session() as session:
            result = session.run(
                """
                CREATE (n:TestNode {message: "Hello Neo4j"})
                RETURN n.message AS message
                """
            )

            record = result.single()

            print("Neo4j connection successful!")
            print("Created node:", record["message"])

    except Exception as e:
        print("Error connecting to Neo4j:")
        print(e)

    finally:
        driver.close()


if __name__ == "__main__":
    create_test_node()

