# Imports
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# hasher method
hasher = PasswordHasher()

#User class and user information
class User:

    # Initialization
    def __init__(self, user_id : int, first_name : str , last_name : str, username : str, email : str, created_at : str, updated_at : str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = None
        self.created_at = created_at
        self.updated_at = updated_at

    # Saving password method
    def set_password(self, password : str) -> None:
        self.password_hash = hasher.hash(password)

    # Password verification method                                    
    def verify_password(self, password : str) -> bool:
        try:
            hasher.verify(self.password_hash, password)
            return True
        except VerifyMismatchError:
            return False
            
