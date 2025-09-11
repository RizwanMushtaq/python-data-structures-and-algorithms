from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional[Node] = None


class LL:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0

    def getSize(self) -> int:
        return self.size

    def addFirst(self, data: int):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.size += 1
            return

        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return

    def addLast(self, data: int):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.size += 1
            return

        currNode = self.head
        while (currNode.next):
            currNode = currNode.next

        currNode.next = newNode
        newNode.next = None
        self.size += 1
        return

    # insert at specific index
    def add(self, index: int, data: int):
        if (index > self.size or index < 0):
            print("Invalid index value")
            return

        newNode = Node(data)
        if (self.head == None or index == 0):
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return

        currNode = self.head
        for i in range(index - 1):  # stop one before target index
            currNode = currNode.next

        nextNode = currNode.next
        currNode.next = newNode
        newNode.next = nextNode
        self.size += 1
        return

    def deleteFirst(self):
        if (self.head == None):
            print("List is empty")
            return

        self.head = self.head.next
        self.size -= 1
        return

    def deleteLast(self):
        if (self.head == None):
            print("List is empty")
            return

        # when there is single element
        if (self.head.next == None):
            self.head = None
            self.size -= 1
            return

        currNode = self.head
        while (currNode.next.next):
            currNode = currNode.next

        currNode.next = None
        self.size -= 1
        return

    # delete at specific index
    def delete(self, index: int):
        if index >= self.size or index < 0:
            print("Invalid Index value")
            return

        if self.size == 0:
            print("List is empty")
            return

        # Case 1: delete head
        if index == 0:
            nextNode = self.head.next
            self.head = nextNode
            self.size -= 1
            return

        # Case 2: delete at index > 0
        currNode = self.head.next
        prevNode = self.head
        for i in range(1, index):  # stop at node before target
            prevNode = currNode
            currNode = currNode.next

        prevNode.next = currNode.next  # bypass the deleted node
        currNode.next = None
        self.size -= 1
        return

    def printList(self):
        if (self.head == None):
            print("List is empty")
            return

        currNode = self.head
        while (currNode):
            print(currNode.data, " -> ", end=" ")
            currNode = currNode.next

        print("NULL")
