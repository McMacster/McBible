__author__ = 'losos'
from . import Logger as log
from .MyMap import MyMap

class Favourites():
    def __init__(self):
        self.content = MyMap() #key - owner, value - list

    def addVerset(self, owner, bookName, bookNr, startingVersetNr, endingVersetNr):
        try:
            for i in self.content.getEntry(owner):
                if i == [bookName, bookNr, startingVersetNr, endingVersetNr]:
                    return
        except ValueError:
            pass
        self.content.addEntry(owner, [bookName, bookNr, startingVersetNr, endingVersetNr])

    def getAllVersets(self, owner):
        return self.content.getEntry(owner)
