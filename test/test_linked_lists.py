from linked_list.linked_list import LinkedList, Node


def test_getting_an_empty_list():
    new_list = LinkedList()
    assert new_list.empty() is True


def test_append_for_two_values():
    new_list = LinkedList()
    new_list.append(Node(3))
    new_list.append(Node(1))
    assert new_list.first_node.value == 3
    assert new_list.first_node.next_node.value == 1

def test_append_for_three_values():
    new_list = LinkedList()
    new_list.append(Node(3))
    new_list.append(Node(1))
    new_list.append(Node(5))
    assert new_list.first_node.value == 3
    assert new_list.first_node.next_node.value == 1
    assert new_list.first_node.next_node.next_node.value == 5

def test_count_on_empty_list_to_zero():
    new_list = LinkedList()
    assert new_list.count() == 0

def test_count_on_list_with_two_node():
    new_list = LinkedList(Node(3, Node(5)))
    assert new_list.count() == 2

def test_create_list_with_no_nodes():
    newlist = LinkedList.create_list()
    assert newlist.empty()

def test_create_list_with_two_nodes():
    newlist = LinkedList.create_list(3 , 5)
    assert newlist.count() == 2
    assert newlist.first_node.value == 3
    newlist.first_node.next_node.value == 5

def test_enumerate_with_no_nodes():
    newlist = LinkedList()
    assert newlist.enumerate()

