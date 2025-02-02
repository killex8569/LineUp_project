class User:

    id = None
    username = None
    passhash = None

    def __init__(self, id: int, username: str, passhash: str):
        self.id = id
        self.username = username
        self.passhash = passhash
    
    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "passhash": self.passhash
        }