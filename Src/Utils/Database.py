__author__ = 'losos'
from . import Logger as log
from .MyMap import MyMap
from collections import OrderedDict

class Testament():
    def __init__(self, orderIndex, bookName, bookNr, verset):
        self.books = MyMap() #map will hold versets
        self.addVerset(orderIndex, bookName, bookNr, verset)
        self.versetIdPos = 0
        self.versetContentPos = 1

    def addVerset(self, orderIndex, bookName, bookNr, verset):
        self.books.addEntry(bookName + bookNr, [orderIndex, verset])

    def getAllBooks(self):
        return self.books.getAllIds()

    def getAllVersets(self, book):
        return self.books.getEntry(book)

    def getAllVersetsIds(self, book):
        return self.books.getEntry(book)

    def getVerset(self, book, versId):
        return self.books.getEntry(book)[versId][self.versetContentPos]

class Bible():
    def __init__(self):
        self.testaments = OrderedDict()
        self.orderIndex = 0

    def addVersets(self, versets):
        for verset in versets:
            self.addVerset(self, verset.testament, verset.bookName, verset.bookNr, verset.verset)

    def addVerset(self, testament, bookName, bookNr, verset):
        log.dbg("Adding testament: " + testament)
        log.dbg("bookName: " + bookName)
        log.dbg("bookNr: " + bookNr)
        log.dbg("verset: " + str(verset))
        if testament in self.testaments:
            log.dbg("Key exists: " + testament)
            self.testaments.get(testament).addVerset(self.orderIndex, bookName, bookNr, verset)
        else:
            log.dbg("New key: " + testament)
            self.testaments[testament] = Testament(self.orderIndex, bookName, bookNr, verset)
        self.orderIndex = self.orderIndex + 1

    def getAllTestaments(self):
        return list(self.testaments)

    def getAllBooks(self, testament):
        return self.testaments[testament].getAllBooks()

    def getAllVers(self, testament, book):
        return self.testaments[testament].getAllVersets(book)

    def getVers(self, testament, book, versId):
        return self.testaments[testament].getVerset(book, versId)

# Bible
#     Testaments
#         Books [name ; number]
#             versets