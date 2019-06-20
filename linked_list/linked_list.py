from typing import Optional


class Node:
    def __init__(self, value: int, next_node: Optional['Node'] = None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, first_node: Optional[Node] = None):
        self.first_node = first_node

    @staticmethod
    def create_list(*args):
        new_list = LinkedList()
        for arg in args:
            new_node = Node(arg)
            new_list.append(new_node)

        return new_list

    def empty(self) -> bool:
        return self.first_node is None

    def append(self, new_node: Node):
        if self.empty():
            self.first_node = new_node
            self.last_added_node = self.first_node
        else:
            self.last_added_node.next_node = new_node
            self.last_added_node = new_node

    def count(self):
        if self.empty():
            return 0

        count = 1
        next_node = self.first_node
        while next_node.next_node != None:
            count = count+1
            next_node = next_node.next_node

        return count

    def enumerate(self):
        ...

    def insert(self):
        ...
