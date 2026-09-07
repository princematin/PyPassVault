# entries :

# id
# user_id
# site_name
# username
# password
# url
# tags
# created_at
# updated_at

class PasswordEntry:
    def __init__(self, id : int, user_id : int, site_name : str, username : str, password : str, url : str, tags : list[str], created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.site_name = site_name
        self.username = username
        self.password = password
        self.url = url
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
