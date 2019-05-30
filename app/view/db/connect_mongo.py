import pymongo
import json

class ConnectDB():
	def __init__(self):
		with open('view/db/mymongo.json') as Json:
			doc = json.loads(Json.read())
		self.mongoURL = str("mongodb+srv://%s:%s%s"%(doc['MongoID'],doc['MongoPassword'],doc['MongoURL']))
		self.client = pymongo.MongoClient(self.mongoURL)
		self.db = pymongo.database.Database(self.client, 'Cluster0')

	def close(self):
		try:
			self.client.close()
			return True
		except:
			return False
