import pymongo
from bson.objectid import ObjectId

class Profile():
    def __init__(self, db):
        self.profile = pymongo.collection.Collection(db, 'Profile')     
    
    def profileValidation(self):
        try:
            profile = self.profile.find()
            return profile
        except:
            return False

    def profileUpdate(self, profileDict):
        print(self.profile.find())
        self.profile.update(
            {"id": "1"},
            {"$set":{"profileName1":profileDict["profileName1"], 
            "profileName2":profileDict["profileName2"], 
            "profileContents":profileDict["profileContents"], 
            "profileTitle":profileDict["profileTitle"]}},
            upsert=False)
        print(self.profile.find())
        return True
        