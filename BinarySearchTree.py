"""
Author: Gray A. LeCompte
Date: 20 November 2017
Description: Implements Binary Search Tree class, subclass of Binary Tree
"""

from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):

    def maxValue(self):
        if self.isEmpty():
            return None
        else:
            if self.getRightChild() is not None:
                return self.getRightChild().maxValue()
            else:
                return self.getData()

    def minValue(self):
        if self.isEmpty():
            return None
        else:
            if self.getLeftChild() is not None:
                return self.getLeftChild().minValue()
            else:
                return self.getData()

    def isBST(self):
        if self.isEmpty():
            return True
        else:
            if self.getLeftChild() is not None and (not self.getLeftChild().isBST() or self.getLeftChild().maxValue()
                >= self.getData()):
                return False
            elif self.getRightChild() is not None and (not self.getRightChild().isBST() or self.getRightChild()
                    .minValue() < self.getData()):
                return False
            else:
                return True

    def insert(self, data):
        if self.isEmpty():
            self.setData(data)
        elif data < self.getData():
            if self.getLeftChild() is None:
                self.setLeftChild(BinarySearchTree(data))
            else:
                self.getLeftChild().insert(data)
        else: # data >= self.getData()
            if self.getRightChild() is None:
                self.setRightChild(BinarySearchTree(data))
            else:
                self.getRightChild().insert(data)

    def retrieve(self, data):
        if self.isEmpty():
            return None
        if self.getData() == data:
            return self.getData()
        else:
            if data < self.getData():
                if self.getLeftChild() is None:
                    return None
                else:
                    return self.getLeftChild().retrieve(data)
            else:
                if self.getRightChild() is None:
                    return None
                else:
                    return self.getRightChild().retrieve(data)


