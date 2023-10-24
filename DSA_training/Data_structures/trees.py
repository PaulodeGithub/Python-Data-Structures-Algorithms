# O(log n) is achieved through dived and conquer
# O (n) is worst case scenario

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        # we will update the root node with the insert method,
        # intitializing an empty tree
        self.root = None