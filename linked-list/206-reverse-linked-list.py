import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        currentNode = head
        nextNode = None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        return previousNode


# ---------- Helper functions ----------
def list_to_linkedlist(items):
    """Convert a Python list to a linked list and return the head."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    """Convert a linked list back to a Python list."""
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


# ---------- Unit tests ----------
class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        head = list_to_linkedlist([])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(linkedlist_to_list(reversed_head), [])

    def test_single_element(self):
        head = list_to_linkedlist([1])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(linkedlist_to_list(reversed_head), [1])

    def test_multiple_elements(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(linkedlist_to_list(reversed_head), [5, 4, 3, 2, 1])

    def test_two_elements(self):
        head = list_to_linkedlist([10, 20])
        reversed_head = self.sol.reverseList(head)
        self.assertEqual(linkedlist_to_list(reversed_head), [20, 10])


if __name__ == "__main__":
    unittest.main()
