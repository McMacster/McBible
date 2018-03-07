__author__ = 'losos'
import unittest
from .Database import *
from . import Logger as log

class BibleTest(unittest.TestCase):
    def setUp(self):
        self.bible = Bible()
        log.turnOff()
        pass

    def addSimpleContent1(self):                                                     #index
        self.bible.addVerset("old testament", "origins", "5", ["1", "verset first"]) #0
        self.bible.addVerset("old testament", "origins", "5", ["2", "verset 2 abc"]) #1
        self.bible.addVerset("old testament", "origins", "5", ["1", "verset 3 def"]) #2
        self.bible.addVerset("old testament", "origins", "5", ["1", "verset last"])  #3

    def addSimpleContent2(self):                                                    #index
        self.bible.addVerset("old testament", "origins", "5", ["7", "+_)("])        #0
        self.bible.addVerset("old testament", "mach", "8", ["6", "-"])              #1
        self.bible.addVerset("old testament", "exodus", "45", ["8", "abcdef."])     #2
        self.bible.addVerset("new testament", "jan", "15", ["1", "aaa"])            #3
        self.bible.addVerset("new testament", "jan", "16", ["2", "bbb"])            #4

    def test_bibleContentEmpty(self):
        self.assertRaises(KeyError, self.bible.getAllBooks, "not existent testament")

    def test_addTestaments(self):
        self.assertEqual(len(self.bible.getAllTestaments()), 0)

        self.bible.addVerset('old testament', "origins", "5", ["1", "verset first"])
        self.assertEqual(len(self.bible.getAllTestaments()), 1)
        self.assertEqual(self.bible.getAllTestaments(), ['old testament'])

        self.bible.addVerset("new testament", "abc", "1", ["1", "verset first"])
        self.assertEqual(len(self.bible.getAllTestaments()), 2)
        self.assertEqual(self.bible.getAllTestaments(), ['old testament', 'new testament'])

        self.bible.addVerset("new testament", "def", "2", ["1", "verset first"])
        self.bible.addVerset("new testament", "xxx", "3", ["1", "verset first"])
        self.bible.addVerset("new testament", "yyy", "4", ["1", "verset first"])
        self.bible.addVerset("new testament", "zzz", "5", ["1", "verset first"])
        self.assertEqual(len(self.bible.getAllTestaments()), 2)
        self.assertEqual(self.bible.getAllTestaments(), ['old testament', 'new testament'])

    def test_bibleContentSimple(self):
        self.addSimpleContent1()
        self.assertEqual(len(self.bible.getAllTestaments()), 1)
        self.assertEqual(self.bible.getAllTestaments(), ["old testament"])
        self.assertEqual(self.bible.getAllBooks("old testament"), ["origins5"])
        self.assertEqual(self.bible.getAllVers("old testament", "origins5"), [[0, ["1", "verset first"]], [1, ["2", "verset 2 abc"]], [2, ["1", "verset 3 def"]], [3, ["1", "verset last"]]])
        self.assertEqual(self.bible.getAllTestaments(), ['old testament'])

    def test_bibleContentExtended(self):
        self.addSimpleContent2()
        self.assertEqual(len(self.bible.getAllTestaments()), 2)
        self.assertEqual(self.bible.getAllTestaments(), ["old testament", "new testament"])
        self.assertEqual(self.bible.getAllBooks("old testament"), ["origins5", "mach8", "exodus45"])
        self.assertEqual(self.bible.getAllBooks("new testament"), ["jan15", "jan16"])
        self.assertEqual(self.bible.getAllVers("old testament", "exodus45"), [[2, ["8", "abcdef."]]])
        self.assertEqual(self.bible.getAllTestaments(), ['old testament', 'new testament'])

    def test_gettingVerset(self):
        self.addSimpleContent1()
        self.assertEqual(self.bible.getVers("old testament", "origins5", 0), ["1", "verset first"])
        self.assertEqual(self.bible.getVers("old testament", "origins5", 1), ["2", "verset 2 abc"])
        self.assertEqual(self.bible.getVers("old testament", "origins5", 2), ["1", "verset 3 def"])
        self.addSimpleContent2()
        # self.assertEqual(self.bible.getVers("old testament", "exodus45", "8"), "abcdef.")

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2)
    unittest.main()