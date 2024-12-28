''' File: HashTableStudentRecordsMain.py
    Author: Clayton Ferner
    Date: 6/14/2017
    Descriptions:  This program will create Hash Table and use either
                   Chaining or Linear Probing for collision resolution.
                   It will read in ids and student names from a
                   file and insert those into the tree, reporting how
                   long it takes to do that.  It then reads ids (no name)
                   from another file, retrieves the data in the tree that
                   matches the ide, and reports how long that took.

                   The program will also iterator over a range of number
                   of records to allow an assessment of the effect of N
                   on the time to insert and retrieve using either
                   collision resolution.
'''

import time
from Hash import *
from Student import Student

# Iterate number of records from NUM_RECORDS_START to NUM_RECORDS_STOP in
# increments of NUM_RECORDS_STEP.

# NUM_RECORDS_START = 20000
# NUM_RECORDS_STOP = 300001
# NUM_RECORDS_STEP = 40000

NUM_RECORDS_START = 200000
NUM_RECORDS_STOP = 3000001
NUM_RECORDS_STEP = 400000

TABLE_SIZE = 320009 # 320009 400009 500009 600011 700001 800011 1000003

UseChaining = True # or UseChaining = False to use a Probing

listOfNamesFileName = "listOfNames.txt"              # Randomized by id
listOfIdsFileName = "searchIds.txt"                  # Randomized by id

def main():

    for nrec in range(NUM_RECORDS_START, NUM_RECORDS_STOP, NUM_RECORDS_STEP):

        # Create the tree
        if (UseChaining):
            theTable = HashTableChaining(TABLE_SIZE)
        else:
            theTable = HashTableProbing(TABLE_SIZE, 11)

        # Open the input file of ids and names
        inputfile = open(listOfNamesFileName, "r")

        startTime = time.time()

        # We are only going to read in nrec number of records
        count = 0
        for line in inputfile:
            if count >= nrec:
                break
            s = line.strip().split(",")

            # The AVL tree requires us to reassign because the root can change
            if (UseChaining):
               theTable.put(Student(int(s[0]), s[1]))
            else:
                theTable.put(Student(int(s[0]), s[1]))
            count += 1

        # Stop the timer, close the file, and report how long it took

        endTime = time.time()

        inputfile.close()

        if (UseChaining):
            print("Time to insert " + str(nrec) + " records into the Hash Table using Chaining: ", end="")
        else:
            print("Time to insert " + str(nrec) + " records into the the Hash Table using Linear Probing: ", end="")

        print ("\t{0:.6f}\tseconds".format(endTime - startTime))

        # print(theTable)   # Useful for testing only

        # Open the input file of ids (only)
        searchfile = open(listOfIdsFileName, "r")

        startTime = time.time()

        # We are only going to read in nrec number of records
        count = 0
        found = 0
        for line in searchfile:

            if count >= nrec:
                break
            s = line.strip().split("\t")
            s1 = theTable.retrieve(Student(int(s[0])))


            if (s1 is not None):
                found += 1

            # Use this for testing
            if (s1 is None):
                print("Couldn't find student id " + str(s[0]))
            #else:
                # print(str(s1))

            count += 1

        # Stop the timer, close the file, and report how long it took
        endTime = time.time()

        searchfile.close()

        print("Found " + str(found) + " of " + str(count) + " searches.")

        if (UseChaining):
            print("Time to retrieve " + str(nrec) + " records from the Hash Table using Chaining: ", end="")
        else:
            print("Time to retrieve " + str(nrec) + " records from a the Hash Table using Linear Probing: ", end="")

        print ("\t{0:.6f}\tseconds".format(endTime - startTime))

main()


