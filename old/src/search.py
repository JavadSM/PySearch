#Copyright@ Javad Shafique 2017
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

'''varibels and data sets'''
#VARS
io_file = "file.io"
'''This is search.cpp binary path'''
search_bin = "bin\search.exe"
#database
file = ".\database.dhp"
with open(file,'r') as file:
    database = ([line.strip() for line in file])

'''Defing Functions'''

#Lowerfile Sytem is case sensitive 
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
#Search¨with search.exe an dump to io_file
def module(word):
    com = search_bin + " " + word + " .\database.dhp >> "+ io_file
    os.system(com)

##SEARCHING FUNTION##
def search(string, results):
    #Erase file
    open(io_file, 'w').close()
    #Split input
    words = split(string)
    #Search with search.exe
    for item in words:
        module(item)
    #Read output
    io = open(io_file, "r")
    io_data = list(io.readlines())
    count = 0
    #And Compare results
    while count != results:
        try:
            base = comp(io_data)
        except ValueError:
            print("No more results")
            break
        io_data = [x for x in io_data if x != base]
        sline = int(base) - 1
        print(database[sline], "On line:", base)
        count += 1