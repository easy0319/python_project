import pymongo
from bson.objectid import ObjectId

class Profile():
    def __init__(self, db):
        self.profile = pymongo.collection.Collection(db, 'Profile')

    def profileValidation(self):
        if self.profile.count() == 0:
            self.profileInit()

        try:
            profile = self.profile.find()
            return profile
        except:
            return False

    def profileInit(self):
        try:
            self.profile.insert_one({
                "profileName1":"Ji-hyeon Lee",
                "profileName2":"Geun-hyeok Oh",
                "profileContents":"beginner programer screendoor",
                "profileTitle":"My Portfolio","id":"1"
                }).inserted_id
            return True
        except:
            return False


    def profileUpdate(self, profileDict):
        self.profile.update(
            {"id": "1"},
            {"$set":{"profileName1":profileDict["profileName1"], 
            "profileName2":profileDict["profileName2"], 
            "profileContents":profileDict["profileContents"], 
            "profileTitle":profileDict["profileTitle"]}},
            upsert=False)
        return True
        