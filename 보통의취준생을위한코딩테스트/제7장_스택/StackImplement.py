
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        add_node = Node(data)

        add_node.next = self.head
        self.head = add_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        
        return ret_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data