from database import get_connection


with open("schema.sql" , "r") as file:
    schema=file.read()
connection=get_connection()
cursor=connection.cursor()
cursor.execute(schema)
connection.commit()
cursor.close()
connection.close()
print("Tables created successfully")