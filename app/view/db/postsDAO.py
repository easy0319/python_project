import pymongo

class Posts():
    def __init__(self, db):
        self.posts = pymongo.collection.Collection(db, 'Posts')
    
    def postValidation(self):
        try:
            posts = self.posts.find()
            return posts
        except:
            return False

    def postCreate(self, postDict):
        try:
            posts = self.posts.insert_one(postDict)
            return posts
        except:
            return False

    def postAuthentication(self, postDict):
        if self.posts.find_one(postDict) is not None:
            return True
        else:
            return False
