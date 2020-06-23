
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def __len__(self):
        return self.length

    def get_max(self):
        if self.head is None:
            return None

        current_maximum = self.head
        current_node = self.head

        while current_node is not None:
            if current_node.next_node is not None:
                if current_node.value >= current_node.next_node.value:
                    current_maximum = current_node
                    current_node = current_node.next_node
                else:
                    current_maximum = current_node.next_node
                    current_node = current_node.next_node
            else:
                return current_maximum.value

    # Add a new item to the head of the list.
    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
        return self

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

        self.length += 1
        return self

    # delete an item from the end
    def remove_head(self):
        if not self.head:
            return None

        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return head_value

        head_value = self.head.value
        self.head = self.head.next_node
        self.length -= 1
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
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
