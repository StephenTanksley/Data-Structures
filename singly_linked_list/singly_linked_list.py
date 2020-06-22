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
