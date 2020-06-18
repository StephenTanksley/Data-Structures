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
# We insert a value into the list at the end by using len(self.storage) to find the greatest index.
#         self.storage.insert(len(self.storage), value)
#         self.size += 1
#         return self.storage

#     def dequeue(self):
#         if(self.size > 0):
#             self.storage.pop(0)
#             self.size -= 1
#             return self.storage
#         else:
#             print("There's nothing to remove.")


# queue = Queue()


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.insert(len(self.storage), value)

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.pop(0)

        else:
            print("There's nothing to remove.")


queue = Queue()


# queue.enqueue(5)

# print("storage length: ", len(queue.storage))
# # queue.enqueue(75)
# # queue.enqueue(6)


# # print(queue.storage)
# # print(queue.__len__())

# # queue.dequeue()
# # queue.dequeue()
# # queue.dequeue()
# # queue.dequeue()

# print(queue.storage)
# print(queue.__len__())
