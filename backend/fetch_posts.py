from elements.user.user import User
from elements.post.post import Post
class FetchPost():
    def __init__(self, db):
        self.__database = db
    
    def getGlobalPosts(self):
        collection = self.__database.postD.find()
        postSet = []
        for i in collection:
            print(i)
            i['user'] = User(self.__database.userD.find_one({'_id': i['user']}))
            
            a = Post(i)
            postSet.append(a.getPostData())

        return postSet

