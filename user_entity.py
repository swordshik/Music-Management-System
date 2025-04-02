class User:

    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password
    
    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password