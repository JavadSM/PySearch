#importing libaries
import os
import time
import itertools
import operator
import glob
#Custom imports
from glob import glob
from itertools import chain
from random import *
#varibels and data sets
file = "database.dhp"
with open(file,'r') as file:
    database = ([line.strip() for line in file])
#Defing Functions
'''
COMMENT
'''
#Lowerfile
def lowerfile(filename):
    file = open(filename, 'r')
    lines = [line.lower() for line in file]
    with open(filename, 'w') as out:
        out.writelines(sorted(lines))
#Compare algorithem
def comp(listen):
    SL = sorted((x, i) for i, x in enumerate(listen))
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(listen)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index
    return max(groups, key=_auxfun)[0]
#Split into words
def split(text):
    words = text.split()
    # List
    return(words)
#Search¨with search.exe an dump to file.io
def module(word):
    com = ".\search.exe " + word + " .\database.dhp >> file.io"
    os.system(com)

##SEARCHING FUNTION##
def search(string, results):
    #Erase file
    open('file.io', 'w').close()
    #Split input
    words = split(string)
    #Search with search.exe
    for item in words:
        module(item)
    #Read output
    io = open("file.io", "r")
    io_data = list(io.readlines())
    count = 0
    #And Compare results
    while count != results:
        try:
            base = comp(io_data)
        except ValueError:
            break
        io_data = [x for x in io_data if x != base]
        sline = int(base) - 1
        print(database[sline], "On line:", base)
        count += 1