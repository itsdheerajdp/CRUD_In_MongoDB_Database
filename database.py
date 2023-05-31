import pymongo
mongoURI="mongodb+srv://singhdheeraj2696:3WfC43uZGKwLIaeI@cluster0.zvxojfa.mongodb.net/"
client=pymongo.MongoClient(mongoURI)
db=client["CRUD_APP"] # this is name of database
collection=db["crud"] # this is name of collection in database

#create operation
def create_task(data):
    response=collection.insert_one(dict(data))
    return response.inserted_id

#read all operation
def read_all():
    response=collection.find({})
    data=[]
    for i in response:
        i['_id']=str(i['_id'])#changing _id(this is in form of object) into string type
        data.append(i)
    return data

#read task of specific id
def read_one(id):
    response=collection.find_one({"id":id})
    if response:
        response['_id']=str(response["_id"]) #changing _id(this is in form of object) into string type
        return response

#update task of specific id
def update(id,updated_task):
    updated_task=dict(updated_task)
    response=collection.update_one({"id":id},{"$set":updated_task})
    return response.modified_count

#delete task of specific id
def delete(id):
    response=collection.delete_one({"id":id})   
    return response.deleted_count