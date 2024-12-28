"""
file: main.py
author: gray a lecompte
date: 20 november 2017
description: this program implements a hash table using a linked list or a binary search tree
    for collision resolution

    a list of student id's and names will be read and inserted into the hash table

    after the names have been inserted the file will close, a new file with just id's will be read
        and the hash table will be searched to retrieve the respective id's and student names

    time will be tracked for bot the insert and retrieval in order to compare the two
    operations
"""

import time
from Hash import *
from HashBST import *
from Student import Student

# Unsorted files
# nameList = "listOfNames.txt" # File containing student name and id
# idList = "searchIds.txt" # File containing just student id

# Sorted files
nameList = "listOfNames_sorted.txt" # File containing student name and id
idList = "searchIds_sorted.txt" # File containing just student id

HASH_TABLE_SIZE = 110007 # += 200000
useBST = False # True to use binary search tree, False to use linked list

def main():

    # if useBST = True
    if useBST:
        hashTable = HashTableBST(HASH_TABLE_SIZE)
    # useBST = False
    else:
        hashTable = HashTableChaining(HASH_TABLE_SIZE)

    """Insert records into hash table"""

    nameFile = open(nameList, "r")  # Open the file containing student names and id's

    startTime = time.time()

    count = 0  # Keep track of the number of records entered into the table

    # Iterate each line in file, split the line values, strip extra characters away
    for line in nameFile:
        data = line.strip().split(",")

        # Insert the student id and name into the hash table and increment counter
        hashTable.put(Student(int(data[0]), data[1]))
        count += 1

    nameFile.close()  # Close the first file

    # Calculate insert execution time
    endTime = time.time()
    insertTime = endTime - startTime

    print("Time to Insert " + str(count) + " Records: " + str(insertTime) + " seconds")

    """ Search records in hash table"""

    startTime = time.time()

    idFile = open(idList, "r") # Open the file containing student names and id's

    count = 0  # Keep track of the number of records entered into the table
    retrieved = 0  # Keep track of the number of successful records found

    # Iterate each line in file, split the line values, strip extra characters away
    for line in idFile:
        data = line.strip().split("\t")

        # Insert the student id and name into the hash table and increment counter
        payload = hashTable.retrieve(Student(int(data[0])))
        count += 1

        if payload is not None:  # If record is found, increment the number of records successfully found
            retrieved += 1

    # Calculate retrieve execution time
    endTime = time.time()
    searchTime = endTime - startTime

    print("Time to Retrieve " + str(retrieved) + " of " + str(count) + " Records: " + str(searchTime) + " seconds")


main()

