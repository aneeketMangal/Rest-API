from elements.user.user import User
from elements.post.post import Post
class PostDatabase():
    def __init__(self, db):
        self.__database = db


    def addPost(self, user:str, content:str, dateTime:str):
        postdata = {'user':user, 'content':content, 'date':dateTime}
        self.__database.postD.insert_one(postdata)

