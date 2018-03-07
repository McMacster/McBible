# -*- coding: utf-8 -*-
__author__ = 'losos'
import unittest
from . import Parser as parser
from . import Logger as log

class ParserTest(unittest.TestCase):
    def setUp(self):
        log.turnOff()
        pass

    def test_invalidLine(self):
        self.assertRaises(ValueError, parser.parse, ">>>New testament")
        self.assertRaises(ValueError, parser.parse, ">>>=============")
        self.assertRaises(ValueError, parser.parse, "    ")
        self.assertRaises(ValueError, parser.parse, "no numbers at all especially on 2nd and 3rd")
        self.assertRaises(ValueError, parser.parse, "12 22 not enough numbers plus book name missing")
        self.assertRaises(ValueError, parser.parse, "abc 12 not enough numbers")
        self.assertRaises(ValueError, parser.parse, "abc 12aa no numbers")

    def test_correctLine(self):
        self.assertEqual(parser.parse('1 Kronik 23 20 Synowie Uzzjela: pierwszy Mika, drugi Jiszszijasz.'),
                         ('1 Kronik', '23', '20', 'Synowie Uzzjela: pierwszy Mika, drugi Jiszszijasz.'))

        self.assertEqual(parser.parse('1 Kronik 23 23 Synowie Musziego — trzej: Machli, Eder i Jeremot.'),
                         ('1 Kronik', '23', '23', 'Synowie Musziego — trzej: Machli, Eder i Jeremot.'))

        self.assertEqual(parser.parse('Mateusza 10  5 Tych to Dwunastu wysłał Jezus, dając im następujące wskazania: "Nie idźcie do pogan i nie wstępujcie do żadnego miasta samarytańskiego.'),
                         ('Mateusza', '10', '5', 'Tych to Dwunastu wysłał Jezus, dając im następujące wskazania: "Nie idźcie do pogan i nie wstępujcie do żadnego miasta samarytańskiego.'))

        self.assertEqual(parser.parse('Malachiasza 4  6 [BT 3:24]  I skłoni serce ojców ku synom, a serce synów ku ich ojcom, abym nie przyszedł i nie poraził ziemi [izraelskiej] przekleństwem.'),
                         ('Malachiasza', '4', '6', ' '.join('[BT 3:24]  I skłoni serce ojców ku synom, a serce synów ku ich ojcom, abym nie przyszedł i nie poraził ziemi [izraelskiej] przekleństwem.'.split())))

        log.turnOff()

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2)
    unittest.main()