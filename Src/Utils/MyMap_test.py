__author__ = 'losos'
from . import Logger as log
import unittest
from .MyMap import MyMap as myMap

class MapTest(unittest.TestCase):
    def setUp(self):
        log.turnOff()
        self.map = myMap()
        self.assertEqual(len(self.map.getAllIds()), 0)
        pass

    def test_mapContentEmpty(self):
        self.assertRaises(ValueError, self.map.getEntry, 7)

    def test_mapContentSimple(self):
        self.map.addEntry(7, "xxx")
        self.map.addEntry(6, "yyy")
        self.map.addEntry(9999, "zzz")
        self.assertEqual(self.map.getEntry(7)[0], "xxx")
        self.assertEqual(self.map.getEntry(6)[0], "yyy")
        self.assertEqual(self.map.getEntry(9999), ["zzz"])

    def test_mapContentExtended(self):
        self.map.addEntry("ab", {"1", "12", "safsf sfd sd sdf"})
        self.map.addEntry("wy", {"7", "6", "-----"})

        self.assertEqual(len(self.map.getEntry("ab")), 1)
        self.assertEqual(len(self.map.getEntry("wy")), 1)

        self.assertEqual(self.map.getEntry("ab")[0], {"1", "12", "safsf sfd sd sdf"})
        self.assertEqual(self.map.getEntry("wy")[0], {"7", "6", "-----"})

        self.map.addEntry("wy", {"next"})
        self.assertEqual(len(self.map.getEntry("ab")), 1)
        self.assertEqual(len(self.map.getEntry("wy")), 2)

        self.assertEqual(self.map.getEntry("wy")[1], {"next"})

        self.assertEqual(self.map.getAllIds()[0], "ab")
        self.assertEqual(self.map.getAllIds()[1], "wy")

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2)
    unittest.main()