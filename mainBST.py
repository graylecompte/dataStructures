from BinarySearchTree import BinarySearchTree
from random import randint
def main():
    BST = BinarySearchTree(5)

    BST.insert(6)
    print(BST)
    BST.insert(4)
    print(BST)
    BST.insert(10)
    print(BST)
    BST.insert(8)
    print(BST)
    BST.insert(3)
    print(BST)

    print(BST.retrieve(4))
    print(BST.minValue())
    print(BST.maxValue())
    print(BST.isBST())

    BST = BinarySearchTree()

    for i in range(0, 101):
        BST.insert(randint(0, 250))

    print(BST)

    for i in range(0, 101):
        print(BST.retrieve(randint(0, 250)))

main()