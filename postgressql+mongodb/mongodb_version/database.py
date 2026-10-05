import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL=os.getenv("MONGO_URL")
client=MongoClient(MONGO_URL)
database=client["task_management"]
project_collection=database["projects"]
task_collection=database["tasks"]
try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("MongoDB connection failed:", e)
print("connected to MongoDB")