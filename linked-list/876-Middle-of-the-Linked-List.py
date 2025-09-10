from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


# ---------- Helper functions ----------
def list_to_linkedlist(items):
    """Convert Python list to linked list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]):
    """Convert linked list back to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ---------- Unit tests ----------
class TestMiddleNode(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_empty_list(self):
        head = list_to_linkedlist([])
        self.assertIsNone(self.sol.middleNode(head))

    def test_single_element(self):
        head = list_to_linkedlist([10])
        mid = self.sol.middleNode(head)
        self.assertEqual(mid.val, 10)

    def test_odd_length_list(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5])
        mid = self.sol.middleNode(head)
        # Middle should be 3
        self.assertEqual(mid.val, 3)
        self.assertEqual(linkedlist_to_list(mid), [3, 4, 5])

    def test_even_length_list(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5, 6])
        mid = self.sol.middleNode(head)
        # For even length, return the second middle (4)
        self.assertEqual(mid.val, 4)
        self.assertEqual(linkedlist_to_list(mid), [4, 5, 6])

    def test_two_elements(self):
        head = list_to_linkedlist([10, 20])
        mid = self.sol.middleNode(head)
        # Second element is the middle
        self.assertEqual(mid.val, 20)


if __name__ == "__main__":
    unittest.main()
