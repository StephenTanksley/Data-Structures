class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None, length=0):
        # Stores a node that corresponds to the first node in the list.
        self.head = None
        # Stores a node that is the end of the list.
        self.tail = None
        self.length = length

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        # create a new node to add
        new_node = Node(value)

        # check to see if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # new_node should point to the current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node
            self.length += 1

    def add_to_tail(self, value):
        # create a new node to add
        new_node = Node(value)
        # check to see if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # point the node at the current tail to the new node
            self.tail.new_node = new_node
            self.tail = new_node
            self.length += 1

    def remove_head(self):
        # if list is empty, do nothing
        if(not self.head):
            return None

        # if list only has one element, set head and tail to None.
        elif self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value

        # 1) store value temporarily: temp = self.head
        # 2) move head or tail pointer next step in: self.head = self.head.next_node
        # 3) remove pointers to next node in the chain temp.next_node = None
        else:
            temp_head = self.head
            self.head = self.head.next_node
            temp_head.next_node = None
            self.length -= 1
            return temp_head.value

    def contains(self, value):
        if self.head is None:
            return False
        else:
            # Loop through each node until we see the value or if we can go no further
            current_node = self.head
            while current_node is not None:
                # check to see if this is the node that we're looking for
                if(current_node == value):
                    return True
                current_node = current_node.next_node
            return False

    def print_list(self):
        current = self.head
        while(current):
            print(f'The current value is {current.value}')
            current = current.next_node


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# Implemented using a list.


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             print("There's nothing to remove.")
#             return None
#         else:
#             removed = self.storage.pop(self.size - 1)
#             self.size -= 1
#             return removed


# Implemented using a Linked List

class Stack:

    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            print("There's nothing to remove.")
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


stack = Stack()
print("--------- push operations -----------")
stack.push(100)
stack.push(101)
stack.push(105)
stack.push(201)
stack.storage.print_list()

print("--------- pop operations -----------")
stack.storage.print_list()
print(stack.pop())

print("--------- revised pop operations -----------")
stack.storage.print_list()


# Should only have 2, 1 returning
# stack.storage.print_list()
