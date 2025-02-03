import json
from ..models.User import User

class DAOUser:

    dbPath = None

    def __init__(self, path):
        self.dbPath = path

    def getAll(self) -> list[User]:
        with open(self.dbPath, 'r') as db:
            data: list[User] = []
            for u in json.load(db)['users']:
                data.append(User(u['id'], u['username'], u['passhash']))
        return data

    
    def getOneById(self, id: int) -> User:
        with open(self.dbPath, 'r') as db:
            for u in json.load(db)['users']:
                if u['id'] == id:
                    return User(u['id'], u['username'], u['passhash'])


    def createOrUpdate(self, user: User) -> bool:
        with open(self.dbPath, 'r+') as db:
            data = json.load(db)
            for i in range(len(data['users'])):
                if user.id == data['users'][i]['id']:
                    data['users'][i] = user.toDict()
                    db.seek(0)
                    json.dump(data, db, ensure_ascii=False, indent=4)
                    return True
            data['users'].append(user.toDict())
            db.seek(0)
            json.dump(data, db, ensure_ascii=False, indent=4)
        return True
    
    
    def delete(self, id: int) -> bool:
        with open(self.dbPath, 'r+') as db:
            data = json.load(db)
            try:
                for i in range(len(data['users'])):
                    if data['users'][i]['id'] == id:
                        del data['users'][i]
            except Exception:
                return False
        with open(self.dbPath, 'w') as db:
            db.seek(0)
            json.dump(data, db, ensure_ascii=False, indent=4)
        return True