class Admin:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password