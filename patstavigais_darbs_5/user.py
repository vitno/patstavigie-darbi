from datetime import datetime


class User:
    def __init__(self, full_name, username, email):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.registered_at = datetime.now()

    def print_user(self):
        result = f"""
        Full name: {self.full_name}
        Username: {self.username}
        E-mail: {self.email}
        Registered at: {self.registered_at} 
        """

        print(result)



