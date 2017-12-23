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
    #make data lowercase for search System because it's casesensitive 
    database = [x.lower() for x in data] #map(str.lower, data)


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
    # returns List
    return(words)

#Searching feture
def searchin(searchfor, data):
    #search for in data
    out = list()
    for i, line in enumerate(data):
        if searchfor in line:
            #check how many times the phrase is in the string
            c = line.count(searchfor)
            while c > 0:
                out.append(i)
                c -= 1
    return out

#Quick search
def search(string, pr = False):
    words = split(string) #split into words
    results = list() #Create results list
    for item in words:
        d = searchin(item, database) # Search for item in data
        for i in d:
            results.append(i)
    #Checks debug config
    if pr:
        print(results)
    #And Compare results
    #varibels 
    i = results
    bl = list()
    maci = len(i)
    #Loop
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
        #Checks debug config
        if pr:
            print(data[item], "in line", item)
    #Returns list with results in order
    return [data[x] for x in bl]

#Find Closest match
def findcl(here, pr = False):
    #Splits word
    cl = list(here)
    #defs out
    out = list()
    #For each letter search and add to list
    for item in cl:
        r = search(item)
        for item in r:
            out.append(item)
    #Compare list and get result
    clo = comp(out)
    #Check debug config
    if pr:
        print(data[clo])
    #return result
    return clo
