__author__ = 'losos'

class MapElement():
    def __init__(self, _id):
        self.ID = _id
        self.CONTENT = list()

    def __enter__(self):
        return self

    def __del__(self):
        pass

    def getID(self):
        return self.ID

    def getContent(self):
        return self.CONTENT

    def push(self, _element):
        self.CONTENT.append(_element)

class MyMap():
    def __init__(self):
        self.mapElements = list()

    def __enter__(self):
        return self

    def __del__(self):
        pass

    # def create(self, _id):
    #     for i in self.mapElements:
    #         if i.getID() == _id:
    #             return
    #     self.mapElements.append(MapElement(_id))

    def addEntry(self, _id, _entry):
        for i in self.mapElements:
            if i.getID() == _id:
                i.push(_entry)
                return
        self.mapElements.append(MapElement(_id))
        self.addEntry(_id, _entry)

    def getEntry(self, _id):
        for i in self.mapElements:
            if i.getID() == _id:
                return i.getContent()
        raise ValueError

    def getAllIds(self):
        ids = list()
        for i in self.mapElements:
            ids.append(i.getID())
        return ids
