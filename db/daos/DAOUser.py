import json

class DAOUser:
    dbPath = None

    def __init__(self, path):
        self.dbPath = path

    def getAll(self):
        with open(self.dbPath, 'r') as db:
            data: list[Playlist] = []
            print(json.load(db))
        return data
