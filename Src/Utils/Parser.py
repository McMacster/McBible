# -*- coding: utf-8 -*-
__author__ = 'losos'
from . import Logger as log

def getMjrIndex(splitted):
    try:
        int(splitted[1])
        return 1
    except:
        try:
            int(splitted[2])
            return 2
        except:
            log.err("No mjr nr in line: " + ' '.join(splitted))
            raise ValueError

def getMinIndex(splitted, mjr):
    try:
        int(splitted[mjr+1])
        return mjr+1
    except:
        log.err("No min nr in line: " + ' '.join(splitted))
        raise ValueError

def parse(line):
    if line[:3] == '>>>':
        log.err("Ommiting comment line: " + line)
        raise ValueError
    splitted = line.split()
    if len(splitted) < 4:
        log.err("Incorrect line: " + line)
        raise ValueError
    mjrId = getMjrIndex(splitted)
    log.dbg(str(splitted))
    minId = getMinIndex(splitted, mjrId)

    book    = ' '.join(splitted[:mjrId])
    majorNr = splitted[mjrId]
    minorNr = splitted[minId]
    meat    = ' '.join(splitted[minId+1:])
    return (book, majorNr, minorNr, meat)


