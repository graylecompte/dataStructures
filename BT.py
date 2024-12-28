"""
file: BT.py
author: gray a lecompte
date: 14 november 2017
description: implements binary tree class
"""

class BinaryTree():
    def __init__(self, data = None, left = None, right = None):
        self.__data = data
        self.__left = left
        self.__right = right

    def __str__(self):
        return self.inorderTraversal()

    def isEmpty(self):
        if self is None or self.__data is None:
            return True
        else:
            return False

    def setData(self, x):
        self.__data = x

    def getData(self):
        if self.isEmpty():
            return None
        else:
            return self.__data

    def getLeftChild(self):
        if self.__left is None:
            return None
        else:
            return self.__left

    def setLeftChild(self, x):
        self.__left = x

    def getRightChild(self):
        if self.__right is None:
            return None
        else:
            return self.__right

    def setRightChild(self, x):
        self.__right = x

    def preorderTraversal(self):
        if self.isEmpty():
            return "Tree is Empty"
        else:
            result = ""
            result += " " + str(self.getData())
            if self.getLeftChild() is not None:
                result += BinaryTree.preorderTraversal(self.getLeftChild())
            if self.getRightChild() is not None:
                result += BinaryTree.preorderTraversal(self.getRightChild())

            return result

    def postorderTraversal(self):
        if self.isEmpty():
            return "Tree is Empty"
        else:
            result = ""
            if self.getLeftChild() is not None:
                result += BinaryTree.inorderTraversal(self.getLeftChild())
            if self.getRightChild() is not None:
                result += BinaryTree.inorderTraversal(self.getRightChild())
            result += " " + str(self.getData())

            return result

    def inorderTraversal(self):
        if self.isEmpty():
            return "Tree is Empty"
        else:
            result = ""
            if self.getLeftChild() is not None:
                result += BinaryTree.inorderTraversal(self.getLeftChild())
            result += " " + str(self.getData())
            if self.getRightChild() is not None:
                result += BinaryTree.inorderTraversal(self.getRightChild())

            return result

