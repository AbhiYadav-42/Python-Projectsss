from cryptography.fernet import Fernet 

class PasswordManger:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict ={}
        
    def create_key(self,path):
        self.key = Fernet.gernate_key()
        print(self.key)
        
pm = PasswordManger()