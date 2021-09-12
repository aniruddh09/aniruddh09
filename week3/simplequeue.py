class Node:
    value: str
    prev: 'Node' = None
    next: 'Node' = None


class SimpleQueue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, value: str):   #assignment
        new_node = Node()
        new_node.value = value
        if self.tail:
            new_node.next = self.tail
            self.tail.prev = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def popleft(self) -> str:     #assignment
        try:
            value = self.head.value
            self.head = self.head.prev
            try:
                self.head.next = None
            except AttributeError:
                self.head = None
            return value
        except:
            return None