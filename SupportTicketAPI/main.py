from fastapi import FastAPI,HTTPException
from typing import Optional,Literal
from pydantic import BaseModel,Field
from bson import ObjectId
from datetime import datetime,timezone
from database import Ticket_collection
from pymongo import ASCENDING


app=FastAPI(
    title="Customer Support Ticket API",
    description="Customer Support API using FASTAPI and MongoDB",
    version="1.0.0"
)

class Customer(BaseModel):
    name:str=Field(...,min_length=3)
    email_id:str|None=None
    phone_no:str

class Comment(BaseModel):
    comment:str=Field(...,min_length=3)
    author:str=Field(...,min_length=3)

class CreateTicket(BaseModel):
    customer:Customer
    title:str=Field(...,min_length=3)
    description:str=Field(...,min_length=3)
    category:str
    priority: Literal[
            "low",
            "medium",
            "high",
            "urgent"
        ] = "medium"
    status:Literal[
            "open",
            "in_progress",
            "resolved",
            "closed"
        ] = "open"
    tags:list[str]=[]

class UpdateTicket(BaseModel):
    title:str=Field(default=None,min_length=3)
    description:str=Field(default=None,min_length=3)
    category:str|None=None
    priority: Literal[
            "low",
            "medium",
            "high",
            "urgent"
        ] |None=None
    tags:list[str]|None=None
class StatusUpdate(BaseModel):
    status:Literal[
            "open",
            "in_progress",
            "resolved",
            "closed"]
            
@app.post("/tickets",status_code=201)
def create_ticket(ticket:CreateTicket):
    current_time=datetime.now(timezone.utc)
    ticket_data={
        "customer":Customer.model_dump(),
        "title":ticket.title,
        "description":ticket.description,
        "category":ticket.category,
        "priority":ticket.priority,
        "status":ticket.status,
        "comments":[],
        "tags":ticket.tags,
        "created_at":current_time,
        "updated_at":current_time
    }
    result=Ticket_collection.insert_one(ticket_data)
    return {
        "message":"Ticket created successfully",
        "ticket_id":str(result.inserted_id)
    }
@app.get("/tickets_data")
def retrieval_tickets():
    tickets=list(Ticket_collection.find())
    for ticket in tickets:
        ticket["id"]=str(ticket["_id"])
        del ticket["_id"]
    return tickets

@app.put("update_tickets/{ticket_id}")
def update_tickets(ticket_id:str,ticket:UpdateTicket):
    try:
        ObjectId=ObjectId(ticket_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid Ticket_id"
        )
    update_data=ticket.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data to update"
        )
    update_data["updated_at"] =(datetime.now(timezone.utc))
        
    result=Ticket_collection.update_one(
        {
            "_id":ObjectId(ticket_id)
        },
        {
            "$set":update_data

            
        }
    )
    if result.matched_count==0:
        raise HTTPException(
            status_code=404,
            detail="Ticket_id not found"
        )
    return {
        "message":"Ticket updated successfully"
    }

@app.delete("delete_ticket/{ticket_id}")
def delete_ticket(ticket_id:str):
    try:
        object_id=ObjectId(ticket_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid ticket_id"
        )
    result=Ticket_collection.delete_one({
        "id":object_id
    })
    if result.deleted_count==0:
        raise HTTPException(
            status_code=404,
            detail="Ticket_id not found"
        )
    return{
        "message":"Ticket deleted successfully",
        "ticket_id":result

    }

@app.post("/adding_comments/{ticket_id}")
def adding_comments(ticket_id:str,comment:Comment):
    try:
        object_id=ObjectId(ticket_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid Ticket_id "
        )
    comment_data={
        "comment":comment.comment,
        "author":comment.author,
        "created_at":datetime.now(timezone.utc)
    }
    result=Ticket_collection.update_one({
        "id":ObjectId
        },
        {
            "$push":{"comments" : comment_data}
        },
        {
            "$set":{"updated_at":datetime.now(timezone.utc)}
        }
        
        )
    if result.matched_count==0:
        raise HTTPException(
                status_code=404,
                detail="Ticket_id not found"
            )
    return{
        "message":"comments added successfully"
        }

@app.patch("/status_update/{ticket_id}")
def status_update(ticket_id:str,status:StatusUpdate):
    try:
        object_id=ObjectId(ticket_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid Ticket_id"
        )
    result=Ticket_collection.update_one({
        "id":object_id
    },
    {
        "$set":{
            "status":status.status,
            "updated_at":datetime.now(timezone.utc)
        }
    }
    )
    if result.matched_count==0:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    return{
        "message":"status updated successfully"
        }

@app.get("/filtering_tickets")
def filter_tickets(priority:str|None=None,status:str|None=None):
    filtered_data={}
    if priority:
        filtered_data["priority"]=priority
    if status:
        filtered_data["status"]=status
    tickets=list(Ticket_collection.find(filtered_data))
    for ticket in tickets:
        ticket["id"]=str(ticket["_id"])
        del ticket["_id"]
    return tickets

@app.get("/search_tickets")
def search_tickets(
    priority:str|None=None,
    status:str|None=None,
    search:str|None=None
):
    filter={}
    if priority:
        filter["priority"]=priority
    if status:
        filter["status"]=status
    if search:
        filter["$or"]=[{
            "title":{
                "$regex":search,
                "$options":"i"
            },
            "description":{
                "$regex":search,
                "$options":"i"
            }
        }]
    tickets=list(Ticket_collection.find(filter))
    for ticket in tickets:
        ticket["id"]=str(ticket["_id"])
        del ticket["_id"]
    return tickets



