__author__ = 'losos'
from . import Logger as log

def openFileForRead(filename):
    try:
        file = open(filename, 'r', encoding='utf-8', errors='ignore')
    except:
        log.err("Cannot open file for read <%s>" % (filename))
        raise
    return file

def openFileForWrite(filename):
    try:
        file = open(filename, 'w', encoding='utf-8')
    except:
        log.err("Cannot open file for write <%s>" % (filename))
        raise
    return file

def appendFile(file, content):
    file.write(content)

def getFileContent(filename):
    fp = openFileForRead(filename)
    return fp.read().splitlines()

def getFileContentRemEmptys(filename):
    return list(filter(None, getFileContent(filename)))

