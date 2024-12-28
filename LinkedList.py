"""
file: LinkedList.py
author: gray a lecompte
date: 14 november 2017
description: implements singly linked list class
"""

class listNode():
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

class LinkedList():
    """Implements a linked list
    """
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert(self, i, x):
        #list is empty, i doesn't matter, node is head and tail
        if self.isEmpty():
            self.__head = listNode(x)
            self.__tail = self.__head
        #insert new node before head, set previous head to next
        elif i <= 0:
            self.__head = listNode(x, self.__head)
        #insert after the tail, previous tail gets a next
        elif i >= self.size():
            self.__tail.setNext(listNode(x))
            self.__tail = self.__tail.getNext()
        #insert at position i
        else:
            current = self.__head
            count = 0
            while (current != None and count < i - 1):
                count += 1
                current = current.getNext()
            current.setNext(listNode(x, current.getNext()))
            if self.__tail == current:
                self.__tail = self.__tail.getNext()
        self.__size += 1 # adds 1 to the size of the list

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def __str__(self):
        result = ""
        current = self.__head
        while current != None:
            result = result + " " + str(current.getData())
            current = current.getNext()
        return result

    def find(self, i):
        current = self.__head
        count = 0
        while current != None and count < i:
            count += 1
            current = current.getNext()
        return current

    def search(self, value):
        current = self.__head
        while current is not None and current.getData() != value:
            current = current.getNext()
        if current is None:
            return None
        else:
            return current.getData()

    def pop(self, i = None):
        if self.isEmpty():
            return None
        else:
            if i == None or i >= self.__size:
                i = self.__size - 1
            if i == 0:
                x = self.__head.getData()
                self.__head = self.__head.getNext()
                self.__size -= 1
                if self.__head == None:
                    self.__tail = None
            else:
                previous = self.find(i - 1)
                x = previous.getNext().getData()
                previous.setNext(previous.getNext().getNext())
                self.__size -= 1
                if previous.getNext() == None:
                    self.__tail = previous
            return x

    def append(self, x):
        self.insert(self.size() + 1, x)

    def prepend(self, x):
        self.insert(0, x)

    def __len__(self):
        return int(self.__size)

    def __getitem__(self, i):
        return self.find(i).getData()

    def __setitem__(self, i, x):
        self.insert(i, x)



