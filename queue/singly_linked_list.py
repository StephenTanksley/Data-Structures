class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)

        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        # point the node at the current tail, to the new node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def print_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next_node


LL = LinkedList()
LL.add_to_tail(3)
LL.add_to_tail(4)
LL.add_to_tail(5)
LL.print_list()

LL.remove_head()
LL.print_list()


# class LinkedList:
#     def __init__(self, head=None, tail=None):
#         # Stores a node that corresponds to the first node in the list.
#         self.head = head
#         # Stores a node that is the end of the list.
#         self.tail = tail

#     def add_to_head(self, value):
#         # create a new node to add
#         new_node = Node(value)

#         # check to see if the list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#             # Both self.head and self.tail are referring to the same node here.
#         else:
#             # new_node should point to the current head
#             new_node.next_node = self.head
#             # move head to new node
#             self.head = new_node

#     def add_to_tail(self, value):
#         # create a new node to add
#         new_node = Node(value)
#         # check to see if the list is empty
#         if self.head is None and self.tail is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # point the node at the current tail to the new node
#             new_node.next_node = self.tail
#             self.tail = new_node

#     def remove_head(self):
#         # if list is empty, do nothing
#         if not self.head:
#             return None
#         # if list only has one element, set head and tail to None.

#         if self.head.next_node is None:
#             head_value = self.head.value
#             self.head = None
#             self.tail = None
#             return head_value
#             # otherwise we have more elements in the list.

#     def contains(self, value):
#         if self.head is None:
#             return False
#         else:
#             # Loop through each node until we see the value or if we can go no further
#             current_node = self.head
#             while current_node is not None:
#                 # check to see if this is the node that we're looking for
#                 if(current_node == value):
#                     return True
#                 current_node = current_node.next_node
#             return False


# linked_list = LinkedList()
