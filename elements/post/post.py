from elements.user.user import User
from database.user_database import UserDatabase
from datetime import datetime

class Post:
    def __init__(self, postDetails):
        self.__userId = postDetails['user']
        self.__content = postDetails['content']
        self.__user = postDetails['user']
        self.__date = postDetails['date']
        
    def updatePost(self, content:str, title:str):
        self.__title = title
        self.__content = "temp" # to be replaced with a parser
        pass

    def getPostData(self):
        return {
            'userImage' : self.__user.getProfilePhotoPath(),
            'user' : self.__user.getUserName(),
            'content' : self.__content,
            'date' : self.__date,
            'image': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'
        }

    def deletePost(self):
        pass
        
    

