import pymongo
import json
import bson

with open('./view/db/mymongo.json') as Json:
	doc = json.loads(Json.read())

mongoURL = str("mongodb+srv://%s:%s%s"%(doc['MongoID'], doc['MongoPassword'], doc["MongoURL"]))
client = pymongo.MongoClient(mongoURL)
db = pymongo.database.Database(client, 'mongoDB')
users = pymongo.collection.Collection(db, 'Users')
