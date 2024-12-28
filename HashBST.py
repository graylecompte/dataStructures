"""
file: HashBST.py
author: gray a lecompte
date: 20 november 2017
description: implements chaining and probing hash table classes
"""

from BinarySearchTree import BinarySearchTree

class HashTableBST():
    """
    Creates a hash table, uses chaining (Binary Search Tree from BST class) for collision resolution
    param: size of the the hash table, if no size is given default size is set to prime number
    """
    def __init__(self, size = None):
        if size is None:
            self.__size = 199 # Prime numbers optimal for hash table size
        else:
            self.__size = size
        # Utilizing binary search tree for collision resolution
        self.__buckets = []
        for i in range(self.__size):
            self.__buckets.append(BinarySearchTree())

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
            self.__buckets[slot].insert(value)

    def retrieve(self, value):
        slot = self.hashValue(value)
        if value is None:
            return None
        # Searches for value in hash table
        else:
            return self.__buckets[slot].retrieve(value)

    def __len__(self):
        return self.__size
