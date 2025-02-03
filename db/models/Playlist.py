class Playlist:

    id = None
    libelle = None
    urlList = None

    def __init__(self, id: int, libelle: str, urlList: list[str]):
        self.id = id
        self.libelle = libelle
        self.urlList = urlList
    
    def toDict(self):
        return {
            "id": self.id,
            "libelle": self.libelle,
            "urlList": self.urlList
        }