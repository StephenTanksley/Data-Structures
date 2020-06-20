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
            temp_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp_head.value

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
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


#  Initialized using a list.

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         added = self.storage.insert(len(self.storage), value)
#         self.size += 1
#         return added

#     def dequeue(self):
#         if(self.size > 0):
#             removed = self.storage.pop(0)
#             self.size -= 1
#             return removed
#         else:
#             print("There's nothing to remove.")


# Implemented using a linked list.

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.__len__()
        # return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        print(f'New value: {value}, queue is {self.size} items long.')
        return self.storage.tail

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            print(f'Item removed. Queue is {self.size} items long.')
            self.storage.remove_head()
        else:
            print("There's nothing to remove.")


# print("head value: ", queue.storage.head.value)
# print("next node: ", queue.storage.head.next_node)
# print("size of the queue: ", queue.size)
queue = Queue()

print("storage length: ", len(queue.storage))

print("----------- queue methods ----------")
queue.enqueue(100)
queue.enqueue(101)
queue.enqueue(105)
queue.enqueue(201)

print("----------- dequeue methods ----------")

queue.dequeue()
queue.dequeue()
queue.dequeue()

# # queue.dequeue()
# # queue.dequeue()

# print(queue.storage)
# print(queue.__len__())
