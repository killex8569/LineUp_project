class Playlist:

    id = None
    libelle = None
    urlList = None

    def __init__(self, id, libelle, urlList):
        self.id = id
        self.libelle = libelle
        self.urlList = urlList