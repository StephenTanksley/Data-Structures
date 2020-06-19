from singly_linked_list import LinkedList

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
            self.storage.remove_head()
            self.size -= 1


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()

# Should only have 2, 1 returning

stack.storage.print_list()
