from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def push_front(self, data):
        new = Node(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self._size += 1

    def print_list(self):
        currHead = self.head
        while currHead != None:
            print(currHead.data, "<-> ", end="")
            currHead = currHead.next


def run_tests():
    dll = DoublyLinkedList()

    # Test size on empty list
    assert dll.size() == 0, f"\nsize(): got: {dll.size()}, want: 0\n"

    # # Test pop_front on empty list
    # assert dll.pop_front() is None, "\npop_front() on empty list should return None\n"

    # # Test pop_back on empty list
    # assert dll.pop_back() is None, "\npop_back() on empty list should return None\n"

    # # Test push_front and size
    # dll.push_front(10)
    # assert dll.size() == 1, f"\nsize(): got: {dll.size()}, want: 1\n"

    # # Test push_back and size
    # dll.push_back(20)
    # assert dll.size() == 2, f"\nsize(): got: {dll.size()}, want: 2\n"

    # # Test contains
    # assert dll.contains(
    #     10) is not None, "\ncontains(10) should find the node\n"
    # assert dll.contains(
    #     30) is None, "\ncontains(30) should not find the node\n"

    # # Test pop_front
    # assert dll.pop_front() == 10, "\npop_front() should return 10\n"
    # assert dll.size() == 1, f"\nsize(): got: {dll.size()}, want: 1\n"

    # # Test pop_back
    # assert dll.pop_back() == 20, "\npop_back() should return 20\n"
    # assert dll.size() == 0, f"\nsize(): got: {dll.size()}, want: 0\n"

    # # Test push_back and pop_back
    # dll.push_back(30)
    # assert dll.pop_back() == 30, "\npop_back() should return 30\n"

    # # Test push_front and pop_front
    # dll.push_front(40)
    # assert dll.pop_front() == 40, "\npop_front() should return 40\n"


run_tests()
