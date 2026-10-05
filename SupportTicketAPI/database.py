import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL=os.getenv("MONGO_URL")
client=MongoClient(MONGO_URL)
database=client["Customer_Support"]
Ticket_collection=database["tickets"]
if __name__=="__main__":
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully")
    except:
        print("MongoDB not connected")
