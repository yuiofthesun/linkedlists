from typing import Optional


class Node:
    def __init__(self, value: int, next_node: Optional['Node']):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, first_node: Optional[Node] = None):
        self.first_node = first_node

    def empty(self) -> bool:
        return self.first_node is None

    def append(self, new_node: Node):
        if self.first_node == None:
            self.first_node = new_node
            self.last_added_node = self.first_node
        else:
            self.last_added_node.next_node = new_node
            self.last_added_node = new_node

    def enumerate(self):
        ...

    def insert(self):
        ...
