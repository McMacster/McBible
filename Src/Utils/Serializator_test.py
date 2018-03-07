# -*- coding: utf-8 -*-
__author__ = 'losos'

# NOTE: this should not be launched as separate module because of serializator constraints
import unittest
from . import Serializator as serial
from . import Logger as log
from . import FileReaderWriiter as fileReader
from . import Database

class Globals():
    def __init__(self):
        self.parentFolder = ""

m = Globals()

class ParserTest(unittest.TestCase):
    def setUp(self):
        log.turnOff()
        self.bible = Database.Bible()
        self.bible.addVerset("One content", "name1", "5", "10 note")
        self.bible.addVerset("One content", "name2", "6", "11 note")
        self.bible.addVerset("One content", "name3", "7", "12 note")
        self.bible.addVerset("Other content", "name4", "8", "13 note")
        self.bible.addVerset("Other content", "name4", "9", "14 note")
        self.bible.addVerset("Yet another content", "name1", "5", "10 note")
        self.bible.addVerset("Yet another content", "name2", "6", "11 note")
        self.bible.addVerset("Yet another content", "name3", "7", "12 note")
        self.bible.addVerset("Yet another content", "name4", "8", "13 note")
        self.bible.addVerset("And another one", "name4", "9", "14 note")
        pass

    def test_serializeString(self):
        a = "just a silly text"
        serial.serialize(m.parentFolder + 'Texts/Tests/entry.pickle', a)
        content = fileReader.getFileContent(m.parentFolder + "Texts/Tests/entry.pickle")
        self.assertGreater(len(content), 0)
        self.assertGreaterEqual(3, len(content))

    def test_serializeStringComplexData(self):
        serial.serialize(m.parentFolder + 'Texts/Tests/bible.pickle', self.bible)
        content = fileReader.getFileContent(m.parentFolder + "Texts/Tests/bible.pickle")
        self.assertGreater(len(content), 10)

    def test_deserializeStringComplexData(self):
        # bible = Database()
        bible = serial.deserialize(m.parentFolder + 'Texts/Tests/bible_tested.pickle') #generated offline by above test (test_serializeStringComplexData)

        self.assertEqual(bible.getAllTestaments(), self.bible.getAllTestaments())
        for testaments in self.bible.getAllTestaments():
            books = self.bible.getAllBooks(testaments)
            self.assertEqual(books, self.bible.getAllBooks(testaments))
            for book in books:
                self.assertEqual(bible.getAllVers(testaments, book), self.bible.getAllVers(testaments, book))

# NOTE: commented - see note at the beginning of file
# if __name__ == "__main__":
#     m.parentFolder = '../'
#     unittest.TextTestRunner(verbosity=2)
#     unittest.main()