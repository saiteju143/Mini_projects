import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
def get_connection():
    connection=psycopg2.connect(DATABASE_URL)
    return connection


if __name__=="__main__":
    connection=get_connection()
    print("Database connected successfully")
    connection.close()