"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

"""
A binary search tree has a few rules.

1) Must be a node-based construct.
2) The left subtree of a node contains only nodes with keys lesser than the original node's key.
3) the right subtree of a node contains only nodes with keys greater than the original node's key.
4) The left and right subtrees of the original node

"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Take the current value of our node
        # Compare to the new value we want to insert.

        # if new_value < self.value
        # if self.left is already taken by a node:
        # make the left node call insert
        # set the left child to the new node with the new value.

        # if new_value >= self.value
        # if self.right is already taken by a node:
        # make the right node call insert
        # set the right child to the new node with the new value.

        # Return True if the tree contains the value
        # False if it does not

        pass

    def contains(self, target):
        """
        # compare the target to current value
        if current.self.value == target:
            return True

        # if the current target is smaller than the current_value:
            go left
            if you can't go left, return False
        # if the current target is greater than the current_value:
            go right
            if you can't go right, return False


        """
        # Start at root.
        # Check to see if the root is the same value as your target.
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
