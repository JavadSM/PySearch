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

#VARS and DATA

#database
with open("database.dhp",'r') as file:
    data = ([line.strip() for line in file])
    database = [x.lower() for x in data] #map(str.lower, data)


#Lowerfile Sytem is case sensitive 
def lowerfile(filename):
    file = open(filename, 'r')
    lines = [line.lower() for line in file]
    with open(filename, 'w') as out:
        out.writelines(sorted(lines))



#Compare algorithem
def comp(listen):
    #Sort list
    SL = sorted((x, i) for i, x in enumerate(listen))
    #Group
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    #Internal functions
    def _auxfun(g):
        #Sort them most first 
        item, iterable = g
        count = 0
        min_index = len(listen)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        return count, -min_index
    #return first in sorted list
    return max(groups, key=_auxfun)[0]



#Split into words
def split(text):
    words = text.split()
    # List
    return(words)


def searchin(searchfor, data):
    #search for in data
    out = list()
    for i, line in enumerate(data):
        if searchfor in line:
            c = line.count(searchfor)
            while c > 0:
                out.append(i)
                c -= 1
    return out

##SEARCHING FUNTION##
def search(string, pr = False):
    words = split(string) #split into words
    results = list() #Create results list
    for item in words:
        d = searchin(item, database) # Search for item in data
        for i in d:
            results.append(i)
    if pr:
        print(results)
    #And Compare results
    i = results
    bl = list()
    maci = len(i)
    while maci > 0:
        #if there is no more results break loop
        try:
            base = comp(i)
        except ValueError:
            break
        #remove last result
        i = [x for x in i if x != base]
        #Append last result
        bl.append(base) 
    #Return data as list with line numbers
    for item in bl:
        if pr:
            print(data[item], "in line", item)
    return bl

def findcl(here, pr = False):
    cl = list(here)
    out = list()
    for item in cl:
        r = search(item)
        for item in r:
            out.append(item)
    clo = comp(out)
    if pr:
        print(data[clo])
    return clo