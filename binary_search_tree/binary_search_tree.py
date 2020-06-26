
"""THIS IS THE QUEUE CLASS """


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        added = self.storage.insert(len(self.storage), value)
        self.size += 1
        return added

    def dequeue(self):
        if(self.size > 0):
            removed = self.storage.pop(0)
            self.size -= 1
            return removed
        else:
            print("There's nothing to remove.")


""" THIS IS THE STACK CLASS """


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            print("There's nothing to remove.")
            return None
        else:
            removed = self.storage.pop(self.size - 1)
            self.size -= 1
            return removed


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
        if(self.left):
            self.left.for_each(fn)
        fn(self.value)
        if(self.right):
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node:
            if node.left:
                node.in_order_print(node.left)
            print(node.value)
            if node.right:
                node.in_order_print(node.right)
        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):

        # 1) - Create a queue for nodes.
        queue = Queue()

        # 1.5) - Check for null values.
        if node.value:

            # 2) - Add the first node to the queue.
            queue.enqueue(node)
            print(queue.storage)

            # 3) - While the queue is not empty
            while queue is not None:

                # 4) - remove the first node from the queue and store it in a current_node variable.
                current_node = queue.dequeue()

                # 5) - print the removed node.
                print(current_node.value)

                # 6) - Add all the children into the queue.
                queue.enqueue(current_node.left)
                queue.enqueue(current_node.right)
            else:
                return

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):

        # 1) - Create a stack for nodes.
        stack = Stack()

        # 2) - Add the first node to the stack.
        stack.push(node)

        # 3) - While the stack is not empty
        while stack is not None:

            # 4) - get the current node from the top of the stack.
            current_node = stack.pop()

            # 5) - print that node.
            print(current_node.value)

            # 6) - add all children to the stack. The order you add the children will matter.
            stack.push(current_node.right)
            stack.push(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
