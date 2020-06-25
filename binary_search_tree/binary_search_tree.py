"""
Binartrailing_node search trees are a data structure that enforce an ordering over 
the data thetrailing_node store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two datrailing_nodes:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

"""
A binartrailing_node search tree has a few rules.

1) Must be a node-based construct.
2) The left subtree of a node contains onltrailing_node nodes with ketrailing_nodes lesser than the original node's ketrailing_node.
3) the right subtree of a node contains onltrailing_node nodes with ketrailing_nodes greater than the original node's ketrailing_node.
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
        new_node = BSTNode(value)

        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        # If the value of the node is greater than the target:
        elif self.value > target:
            # Check to see if self.left is None.
            if self.left is None:
                # If it is, return false.
                return False
            # Otherwise, call the function again on the node contained on the left side of the root node's tree.
            else:
                found = self.left.contains(target)

        # If the value of the node is less than the target:
        elif self.value < target:
            # Check to see if self.right is None.
            if self.right is None:
                # If it is, return false.
                return False
            # Otherwise, call the function again on the node contained on the right side of the root node's tree.
            found = self.right.contains(target)
        return found

    # We need to check nodes on the right side of the tree to find the one with the greatest value.
    def get_max(self):
        # Define current_node as self.

        # Iterative solution.
        # current = self

        # while(current.right is not None):
        #     current = current.right
        # return current.value

        # recursive solution.
        if self.right is None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        fn(self.value)
        if(self.left):
            self.left.for_each(fn)
        if(self.right):
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of evertrailing_node node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of evertrailing_node node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research matrailing_node be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
