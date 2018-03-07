__author__ = 'losos'
import Database
import Logger as log
from MyMap import MyMap

def searchBible(words, bible):
    if type(bible) is not Database.Bible:
        raise TypeError

    searchResult = Database.Bible()
    for testament in bible.getAllTestaments()
        searchResult.addVerset(searchTestamemnt(words, testament))

def searchTestamemnt(words, testament):
    if type(testament) is not Database.Testament:
        raise TypeError
