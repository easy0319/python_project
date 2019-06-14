import pymongo
from bson.objectid import ObjectId

class Posts():
	def __init__(self,db):
		self.posts = pymongo.collection.Collection(db, 'Posts')

	def postCreate(self,postDict):
		try:
			obj_id = self.posts.insert_one(postDict).inserted_id
			return obj_id
		except:
			return False

	def postDelete(self,obj_id):
		try:
			self.posts.delete_one({"_id":ObjectId(obj_id)})
			return True
		except:
			return False

	def postUpdate(self,postDict):
		self.posts.find_and_modify(
			{"_id": ObjectId(postDict["obj_id"])},
			{"$set":{"postTitle":postDict["postTitle"],"postContent":postDict["postContent"]}},
			upsert=False
			)
		return True

	def getAllposts(self):
		try:
			result = self.posts.find().sort("date",-1)
			return result
		except:
			return False

	def getPostsCount(self):
		try:
			result = self.posts.count()
			return result
		except:
			return False

	def getOneposts(self, title, content):
		result = self.posts.find({"postTitle" : title, "postContent" : content})
		if result is not None:
			try:
				return result
			except:
				return False

	def commentCreate(self, title, content, commentDict):
		try:
			self.posts.update({"postTitle" : title, "postContent" : content}, { "$push" : commentDict})
			return True
		except:
			return False
