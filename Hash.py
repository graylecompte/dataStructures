"""
file: Hash.py
author: gray a lecompte
date: 20 november 2017
description: implements chaining and probing hash table classes
"""

from LinkedList import LinkedList

class HashTableChaining():
    """
    Creates a hash table, uses chaining (linked list from LinkedList class) for collision resolution
    param: size of the the hash table, if no size is given default size is set to prime number
    """
    def __init__(self, size = None):
        if size is None:
            self.__size = 199 # Prime numbers optimal for hash table size
        else:
            self.__size = size
        # Utilizing linked list for collision resolution
        self.__buckets = []
        for i in range(self.__size):
            self.__buckets.append(LinkedList())

    def isEmpty(self, value):
        """
        Checks if the location is empty or not
        return: True if there is no value at location
                False otherwise
        """
        if self.retrieve(value) is None:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns the hash table buckets and contents as a string
        """
        result = ""
        for i in range(self.__size):
            result += "bucket " + str(i) + ": " + "\nsize: " + str(self.__buckets[i].size()) + "\n" + str(self.__buckets[i])
        return result

    def hashValue(self, value):
        """
        Calculates the hash value
        param: value to calculate location 
        return: location to place value in hash table
        """
        if value is None:
            return None
        else:
            return value.getId() % self.__size

    def put(self, value):
        """
        Inserts value into hash table
        param: value to be inserted into the table 
        return: None if no value provided
        """
        slot = self.hashValue(value)
        if value is None:
            return None
        # Assigns value to the bucket
        else:
            self.__buckets[slot].append(value)

    def retrieve(self, value):
        slot = self.hashValue(value)
        if value is None:
            return None
        # Searches for value in hash table
        else:
            return self.__buckets[slot].search(value)

    def __len__(self):
        return self.__size

class HashTableProbing():
    """
    Creates a hash table, uses probing for collision resolution
    param: size of the the hash table, if no size is given default size is set to prime number
            size of skip 
    """
    def __init__(self, size = None, skip = None):
        if size is None:
            self.__size = 199 # Prime numbers optimal for hash table size
        else:
            self.__size = size
        # Utilizing linked list for collision resolution
        self.__buckets = []
        # Creates empty hash table with None values
        for i in range(self.__size):
            self.__buckets.append(None)
        # If no skip size is chosen, default is 1
        if skip is None:
            self.__skip = 1
        else:
            self.__skip = skip

    def isEmpty(self, value):
        """
        Checks if the location is empty or not
        return: True if there is no value at location
                False otherwise
        """
        if self.retrieve(value) is None:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns the hash table position and contents as a string
        """
        result = ""
        for i in range(self.__size):
            result += "position " + str(i) + ": " + "\n" + str(self.__buckets[i])
        return result

    def hashValue(self, value):
        """
        Calculates the hash value
        param: value to calculate location 
        return: location to place value in hash table
        """
        if value is None:
            return None
        else:
            return value.getId() % self.__size

    def put(self, value):
        slot = self.hashValue(value)
        initialSlot = slot # Keeps the first position value attempts to go to
        if value is None:
            return None
        # If the bucket is empty assign the value
        if self.__buckets[slot] is None:
            self.__buckets[slot] = value
        else:
            # Iterate through hash table to find next available slot
            while self.__buckets[slot] is not None:
                # Add skip value to current slot
                slot += self.__skip
                # If the end of the list is reached loop to beginning plus the value of skip left
                if slot > self.__size - 1:
                    slot = slot - self.__size - 1
                # Empty bucket is found assign the value
                if self.__buckets[slot] is None:
                    self.__buckets[slot] = value
                    return
                # When the first position is reached again quit
                if slot == initialSlot:
                    return

    def retrieve(self, value):
        slot = self.hashValue(value)
        initialSlot = slot # Keeps the first position value attempts to go to
        if value is None:
            return None
        # If the bucket is empty and not filled with another value
        if self.__buckets[slot] is None:
            return None
        # Value has been found
        if self.__buckets[slot] == value:
            return self.__buckets[slot]
        else:
            # Iterate through hash table to see if value is in a different bucket
            while self.__buckets[slot] is not None and self.__buckets is not value:
                # Add skip value to current slot
                slot += self.__skip
                # If the end of the list is reached loop to beginning plus the value of skip left
                if slot > self.__size - 1:
                    slot = slot - self.__size - 1
                # Value has been found
                if self.__buckets[slot] == value:
                    return self.__buckets[slot]
                # Value was not found
                if slot == initialSlot:
                    return

    def __len__(self):
        return self.__size

class HashTableBST(HashTableChaining):


    def put(self, value):
        """
        Inserts value into hash table
        param: value to be inserted into the table 
        return: None if no value provided
        """
        slot = self.hashValue(value)
        if value is None:
            return None
        # Assigns value to the bucket
        else:
            self.__buckets[slot].insert(value)

    def retrieve(self, value):
        slot = self.hashValue(value)
        if value is None:
            return None
        # Searches for value in hash table
        else:
            return self.__buckets[slot].retrieve(value)