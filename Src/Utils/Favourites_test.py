__author__ = 'losos'
import unittest
from .Favourites import *
from . import Logger as log

class FavouritesTest(unittest.TestCase):
    def setUp(self):
        self.favourites = Favourites()
        log.turnOff()

    def addSimpleContent1(self):
        self.favourites.addVerset("owner a", "a", "1", "1", "1")
        self.favourites.addVerset("owner a", "b", "2", "3", "5")
        self.favourites.addVerset("owner a", "c", "3", "5", "10")
        self.favourites.addVerset("owner a", "d", "4", "7", "50")

    def addSimpleContent2(self):
        self.favourites.addVerset("owner a", "old testament", "c1", "2", "10")
        self.favourites.addVerset("owner b", "old testament", "c1", "4", "15")
        self.favourites.addVerset("owner a", "old testament", "c2", "6", "20")
        self.favourites.addVerset("owner c", "new testament", "c2", "8", "25")
        self.favourites.addVerset("owner a", "new testament", "c3", "10", "30")
        self.favourites.addVerset("owner d", "new testament", "c4", "12", "35")

    def test_favouritesContentEmpty(self):
        self.assertRaises(ValueError, self.favourites.getAllVersets, "not existent owner")

    def test_favouritesSimple1(self):
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner a")
        self.addSimpleContent1()
        self.assertEqual(self.favourites.getAllVersets("owner a"),
                         [  ["a", "1", "1", "1"],
                            ["b", "2", "3", "5"],
                            ["c", "3", "5", "10"],
                            ["d", "4", "7", "50"]])

    def test_favouritesSimple2(self):
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner a")
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner b")
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner c")
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner d")
        self.addSimpleContent2()
        self.assertEqual(self.favourites.getAllVersets("owner a"),
                         [
                            ["old testament", "c1", "2", "10"],
                            ["old testament", "c2", "6", "20"],
                            ["new testament", "c3", "10", "30"]])

        self.assertEqual(self.favourites.getAllVersets("owner b"), [["old testament", "c1", "4", "15"]])
        self.assertEqual(self.favourites.getAllVersets("owner c"), [["new testament", "c2", "8", "25"]])
        self.assertEqual(self.favourites.getAllVersets("owner d"), [["new testament", "c4", "12", "35"]])

    def test_favouritesAddTwice(self):
        self.assertRaises(ValueError, self.favourites.getAllVersets, "owner a")
        self.favourites.addVerset("owner a", "old testament", "c1", "2", "10")
        self.favourites.addVerset("owner a", "old testament", "c1", "2", "10")
        self.assertEqual(self.favourites.getAllVersets("owner a"), [["old testament", "c1", "2", "10"]])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2)
    unittest.main()