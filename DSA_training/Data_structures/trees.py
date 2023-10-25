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

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # if self.root is None: # not neccesary, while loop handles this 
        #     return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(43)
my_tree.insert(24)
my_tree.insert(54)
my_tree.insert(64)

# print(my_tree.root.value)
# print (my_tree.root.left.value)
# print (my_tree.root.right.value)
# print (my_tree.root.right.right.value)