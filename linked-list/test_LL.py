import unittest
from LL import LL


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LL()

    def list_to_array(self):
        """Helper function to return LL elements as a Python list for easier assertions"""
        result = []
        curr = self.ll.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def test_addFirst(self):
        self.ll.addFirst(10)
        self.ll.addFirst(20)
        self.ll.addFirst(30)
        self.assertEqual(self.list_to_array(), [30, 20, 10])
        self.assertEqual(self.ll.getSize(), 3)

    def test_addLast(self):
        self.ll.addLast(1)
        self.ll.addLast(2)
        self.ll.addLast(3)
        self.assertEqual(self.list_to_array(), [1, 2, 3])
        self.assertEqual(self.ll.getSize(), 3)

    def test_add_at_index(self):
        self.ll.addLast(1)
        self.ll.addLast(3)
        self.ll.add(1, 2)   # insert at index 1
        self.assertEqual(self.list_to_array(), [1, 2, 3])
        self.assertEqual(self.ll.getSize(), 3)

        self.ll.add(0, 0)   # insert at head
        self.assertEqual(self.list_to_array(), [0, 1, 2, 3])

        self.ll.add(self.ll.getSize(), 4)  # insert at tail
        self.assertEqual(self.list_to_array(), [0, 1, 2, 3, 4])

    def test_deleteFirst(self):
        self.ll.addLast(1)
        self.ll.addLast(2)
        self.ll.deleteFirst()
        self.assertEqual(self.list_to_array(), [2])
        self.assertEqual(self.ll.getSize(), 1)

    def test_deleteLast(self):
        self.ll.addLast(1)
        self.ll.addLast(2)
        self.ll.addLast(3)
        self.ll.deleteLast()
        self.assertEqual(self.list_to_array(), [1, 2])
        self.assertEqual(self.ll.getSize(), 2)

    def test_delete_at_index(self):
        for i in range(5):
            self.ll.addLast(i)  # list = [0,1,2,3,4]

        self.ll.delete(0)  # delete head
        self.assertEqual(self.list_to_array(), [1, 2, 3, 4])

        self.ll.delete(2)  # delete index 2 (value 3)
        self.assertEqual(self.list_to_array(), [1, 2, 4])

        self.ll.delete(self.ll.getSize() - 1)  # delete last element
        self.assertEqual(self.list_to_array(), [1, 2])

    def test_empty_delete(self):
        self.ll.deleteFirst()   # deleting from empty list
        self.ll.deleteLast()
        self.ll.delete(0)
        self.assertEqual(self.list_to_array(), [])
        self.assertEqual(self.ll.getSize(), 0)


if __name__ == "__main__":
    unittest.main()
