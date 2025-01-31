class User:

    id = None
    username = None
    passhash = None

    def __init__(self, id: int, username: str, passhash: str):
        self.id = id
        self.username = username
        self.passhash = passhash