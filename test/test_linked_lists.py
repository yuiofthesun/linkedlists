from linked_list.linked_list import LinkedList, Node


def test_getting_an_empty_list():
    new_list = LinkedList()
    assert new_list.empty() is True


def test_append_for_two_values():
    new_list = LinkedList()
    new_list.append(Node(3, None))
    new_list.append(Node(1, None))
    assert new_list.first_node.value == 3
    assert new_list.first_node.next_node.value == 1

def test_append_for_three_values():
    new_list = LinkedList()
    new_list.append(Node(3, None))
    new_list.append(Node(1, None))
    new_list.append(Node(5, None))
    assert new_list.first_node.value == 3
    assert new_list.first_node.next_node.value == 1
    assert new_list.first_node.next_node.next_node.value == 5
