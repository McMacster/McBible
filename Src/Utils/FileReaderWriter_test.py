__author__ = 'losos'
import unittest
from . import FileReaderWriiter as fileReader
from . import Logger as logger

class Globals():
    def __init__(self):
        self.parentFolder = ""

m = Globals()

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        logger.turnOff()
        self.testFileContent = fileReader.getFileContent(m.parentFolder + "Texts/Tests/testFile.txt")
        self.testFileContentNoEmptyLines = fileReader.getFileContentRemEmptys(m.parentFolder + "Texts/Tests/testFile.txt")
        self.bibleTestContentOld = fileReader.getFileContent(m.parentFolder + "Texts/Tests/bbl_short_test_old.txt")
        self.bibleTestContentNew = fileReader.getFileContent(m.parentFolder + "Texts/Tests/bbl_short_test_new.txt")
        self.testFilePL = fileReader.getFileContent(m.parentFolder + "Texts/Tests/plikTestowyPl.txt")
        self.testFilePLNowEmptys = fileReader.getFileContentRemEmptys(m.parentFolder + "Texts/Tests/plikTestowyPl.txt")

    def emptyString(self, text):
        return text == ""

    def test_fileDontExist(self):
        self.assertRaises(IOError, fileReader.getFileContent, "fake_file")

    def test_fileOpen(self):
        self.assertTrue(len(self.testFileContent) >= 17 and len(self.testFileContent) <= 18) #in linux splitlines counts different than in win
        self.assertEqual(len(self.bibleTestContentOld), 236)
        self.assertEqual(len(self.bibleTestContentNew), 191)

    def test_filledLinesCheck(self):
        # i = 0
        # for line in self.testFileContent:
        #     print str(i) + ": " + line + '<ENDL>'
        #     i = i +1
        self.assertEqual(self.testFileContent[0], '1: 2 nelines')
        self.assertEqual(self.testFileContent[3], '4: cr newline#1')
        # self.assertEqual(self.testFileContent[5], '6: cr newline#2') #different in linux and win - impossible to port ultimate solution
        # self.assertEqual(self.testFileContent[6], '7: next is cr')

    def test_filledLinesCheckEmptyRemoved(self):
        # i = 0
        # for line in self.testFileContentNoEmplyLines:
        #     print str(i) + ": " + line + '<ENDL>'
        #     i = i +1
        self.assertEqual(self.testFileContentNoEmptyLines[0], '1: 2 nelines')
        self.assertEqual(self.testFileContentNoEmptyLines[1], '4: cr newline#1')
        self.assertEqual(self.testFileContentNoEmptyLines[2], '6: cr newline#2')
        self.assertEqual(self.testFileContentNoEmptyLines[3], '7: next is cr')
        self.assertEqual(self.testFileContentNoEmptyLines[4], '9: lf cr newline')
        self.assertEqual(self.testFileContentNoEmptyLines[5], '10: lf newline#1')
        self.assertEqual(self.testFileContentNoEmptyLines[6], '13: next is lr:')
        self.assertEqual(self.testFileContentNoEmptyLines[7], '16: lf newline#2')
        self.assertEqual(self.testFileContentNoEmptyLines[8], '18: endfile')

    def test_polishSymbols(self):
        self.assertEqual(self.testFilePL[0], 'czekać')
        self.assertEqual(self.testFilePL[2], 'źdźbło')
        self.assertEqual(self.testFilePL[4], 'żółtko')
        self.assertEqual(self.testFilePL[6], 'ąęóźżłńć')

        self.assertEqual(self.testFilePLNowEmptys[0], 'czekać')
        self.assertEqual(self.testFilePLNowEmptys[1], 'źdźbło')
        self.assertEqual(self.testFilePLNowEmptys[2], 'żółtko')
        self.assertEqual(self.testFilePLNowEmptys[3], 'ąęóźżłńć')

    def test_polishSymbolsInAllFiles(self):
        completeNew = fileReader.getFileContent(m.parentFolder + "Texts/Bible/bbl_new.txt")
        completeOld = fileReader.getFileContent(m.parentFolder + "Texts/Bible/bbl_old.txt")
        self.assertEqual(self.bibleTestContentNew[0], '>>>Chrześcijańskie Pisma Greckie - Nowy Testament:')
        self.assertEqual(completeNew[0],              '>>>Chrześcijańskie Pisma Greckie - Nowy Testament:')
        self.assertEqual(self.bibleTestContentOld[3], 'Rodzaju 1  1 Na początku Bóg stworzył niebo i ziemię.')
        self.assertEqual(completeOld[3],              'Rodzaju 1  1 Na początku Bóg stworzył niebo i ziemię.')

if __name__ == "__main__":
    m.parentFolder = "../"
    unittest.TextTestRunner(verbosity=2)
    unittest.main()