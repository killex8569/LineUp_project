import json
from ..models.Playlist import Playlist

class DAOPlaylist:
    
    dbPath = None

    def __init__(self, path):
        self.dbPath = path

    def getAll(self) -> list[Playlist]:
        with open(self.dbPath, 'r') as db:
            data: list[Playlist] = []
            for p in json.load(db)['playlists']:
                data.append(Playlist(p['id'], p['libelle'], p['urlList']))
        return data

    
    def getOneById(self, id: int) -> Playlist:
        with open(self.dbPath, 'r') as db:
            for p in json.load(db)['playlists']:
                if p['id'] == id:
                    return Playlist(Playlist(p['id'], p['libelle'], p['urlList']))


    def createOrUpdate(self, playlist: Playlist) -> bool:
        with open(self.dbPath, 'r+') as db:
            data = json.load(db)
            for i in range(len(data['playlists'])):
                if playlist.id == data['playlists'][i]['id']:
                    data['playlists'][i] = playlist.toDict()
                    db.seek(0)
                    json.dump(data, db, ensure_ascii=False, indent=4)
                    return True
            data['playlists'].append(playlist.toDict())
            db.seek(0)
            json.dump(data, db, ensure_ascii=False, indent=4)
        return True
    
    
    def delete(self, id: int) -> bool:
        with open(self.dbPath, 'r+') as db:
            data = json.load(db)
            try:
                for i in range(len(data['playlists'])):
                    if data['playlists'][i]['id'] == id:
                        del data['playlists'][i]
            except Exception:
                return False
        with open(self.dbPath, 'w') as db:
            db.seek(0)
            json.dump(data, db, ensure_ascii=False, indent=4)
        return True
