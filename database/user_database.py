from elements.user.user import User
class UserDatabase():
    def __init__(self, db):
        self.__database = db


    def test(self):
        self.__database.test.insert_one({'info':'success'})


    def addUser(self, username:str, password:str, pfp = "https://www.seekpng.com/png/detail/143-1435868_headshot-silhouette-person-placeholder.png"):
        userdata = {'username':username, 'pfp':pfp, 'friends': [], 'validated': False, 'password': password}
        self.__database.userD.insert_one(userdata)



    def checkUserAvailability(self, username:str, email:str):
        if(self.__database.userD.find_one({'username': username})):
            return {'isAvailable': False, 'errorLog': "Username is already Taken"}
        elif(self.__database.userD.find_one({'username': username})):
            return {'isAvailable': False, 'errorLog': "Email is already Taken"}
        else:
            return {'isAvailable': True}

    def __getUserData(self, username:str, password:str):
        try:
            return self.__database.userD.find_one({'username': username, 'password': password})
        except:
            return {'errorLog': 'Server Error'}



    def verifyUserDetails(self, username:str, password:str):
        isUser = self.__getUserData(username, password)
        if(isUser):
            return {'isAvailable': True ,'userData': isUser}
        
        else:
            return {'isAvailable': False, 'errorLog': "User details not verfied"}

    
