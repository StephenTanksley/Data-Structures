
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
        print(
            f'New value: {self.storage.tail.value}, queue is {self.size} items long.')
        return self.storage.tail

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            print(f'Item removed. Queue is {self.size} items long.')
            item = self.storage.remove_head()
            print(item)
            return item
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

print("storage length: ", len(queue.storage))

print("----------- dequeue methods ----------")

queue.dequeue()
queue.dequeue()
queue.dequeue()
print("storage length: ", len(queue.storage))

# # queue.dequeue()
# # queue.dequeue()

# print(queue.storage)
# print(queue.__len__())
