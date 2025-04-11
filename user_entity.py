class User:

    def __init__(self, username, email,  password):
        self.username = username
        self.email = email
        self.__password = password

    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password