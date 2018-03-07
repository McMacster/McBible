# -*- coding: utf-8 -*-
__author__ = 'losos'
import Utils.Logger as log
import Utils.FileReaderWriiter as fileReader
import Utils.Parser as parser
import Utils.Database as database
import Utils.Serializator as serial
import time

def readBible(oldFile, newFile):
    contentOld = fileReader.getFileContentRemEmptys(oldFile)
    contentNew = fileReader.getFileContentRemEmptys(newFile)
    bible = database.Bible()
    ommitedLinesOld = 0
    ommitedLinesNew = 0
    for line in contentOld:
        try:
            parsed = parser.parse(line)
            bible.addVerset("Stary Testament", parsed[0], parsed[1], [parsed[2], parsed[3]])
        except ValueError:
            ommitedLinesOld = ommitedLinesOld + 1

    for line in contentNew:
        try:
            parsed = parser.parse(line)
            bible.addVerset("Stary Testament", parsed[0], parsed[1], [parsed[2], parsed[3]])
        except ValueError:
            ommitedLinesNew = ommitedLinesNew + 1

    log.inf("Ommited: old " + str(ommitedLinesOld))
    log.inf("Ommited: new " + str(ommitedLinesNew))
    return bible

def printOutput(filename, bible):
    out = fileReader.openFileForWrite(filename)
    for testament in bible.getAllTestaments():
        fileReader.appendFile(out, testament + "\n")
        for book in bible.getAllBooks(testament):
            fileReader.appendFile(out, book + '\n')
            for vers in bible.getAllVers(testament, book):
                fileReader.appendFile(out, vers[1][0] + ' ' + vers[1][1] + '\n')

def timeStart():
    return time.time()

def timeStop(start_time, note):
    elapsed_time = time.time() - start_time
    log.turnOn()
    log.inf("time for " + note + ": " + str(elapsed_time) + " s")
    log.turnOff()

def doTheStuff():
    log.turnOff()
    log.dbgMode(False)

    t1 = timeStart()
    bible = readBible("Texts/Tests/bbl_short_test_old.txt", "Texts/Tests/bbl_short_test_new.txt")
    timeStop(t1, "read short version")
    printOutput("output_tst.txt", bible)

    t1 = timeStart()
    serial.serialize("data.bin", bible)
    timeStop(t1, "serialize short version")

    t1 = timeStart()
    deserializedBible = serial.deserialize("data.bin")
    timeStop(t1, "deserialize short version")
    printOutput("deserialized.txt", deserializedBible)

    t1 = timeStart()
    bible = readBible("Texts/Bible/bbl_old.txt", "Texts/Bible/bbl_new.txt")
    timeStop(t1, "read full version")
    printOutput("output.txt", bible)

    t1 = timeStart()
    serial.serialize("data_full.bin", bible)
    timeStop(t1, "serialize full version")

    t1 = timeStart()
    deserializedBible = serial.deserialize("data_full.bin")
    timeStop(t1, "deserialize full version")
    printOutput("deserialized_full.txt", deserializedBible)

if __name__ == "__main__":
    doTheStuff()
