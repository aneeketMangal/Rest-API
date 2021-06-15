from elements.user.user import User
from datetime import datetime

class Post:
    def __init__(self, user: User):
        self.__user = user
        self.__title = "New Blog"
        self.__content = [["Type new blog"]]
        self.__date = datetime.now()
        
    def updatePost(self, content:str, title:str):
        self.__title = title
        self.__content = "temp" # to be replaced with a parser
        pass

    def deletePost(self):
        pass
        
    

