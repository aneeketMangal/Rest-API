class User():
    def __init__(self, username:str, pfp:str):
        self.__username = username
        self.__pfp = pfp
    def getUserName(self):
        return self.__username
    def getProfilePhotoPath(self):
        return self.__pfp
    def setUserName(self, newUserName:str):
        self.__username = newUserName
    def setProfilePhotoPath(self, newpfp:str):
        self.__pfp = newpfp

