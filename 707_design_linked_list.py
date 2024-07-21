''' 
Design Linked List
Leetcode # 707
vsulli
21 July 2024

Design your implementation of the linked list. 
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have 
two attributes: val and next. val is the value 
of the current node, and next is a pointer/reference 
to the next node.
If you want to use the doubly linked list, you will 
need one more attribute prev to indicate the previous 
node in the linked list. Assume all nodes in the 
linked list are 0-indexed.
'''



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        # Dummy Node
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        # if index does not exist
        return -1

    def addAtHead(self, val: int) -> None:
        # create new node
        inserted_node = Node(val)

        # its next will be current list excluding dummy
        inserted_node.next = self.head.next

        # set dummy pointer to new node
        self.head.next = inserted_node

        # if list empty before inserting
        if not inserted_node.next:
            self.tail = inserted_node

    def addAtTail(self, val: int) -> None:
        # list empty, tail points to dummy node
        # also works for real node
        self.tail = Node(val)
        self.tail = self.tail.next


    def addAtIndex(self, index: int, val: int) -> None:
        if (index == 0):
            self.addAtHead(val)

        i = 0
        curr = self.head
        # go to node before insertion
        while curr != None and i + 1 != index:
            i += 1
            curr = curr.next
        
        if curr != None:
            inserted_node = Node(val)
            inserted_node.next = curr.next
            curr.next = inserted_node


    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head

        while curr:
            # get to node before removal
            while i < index and curr:
                i += 1
                curr = curr.next

        # node before and target node exist
        if curr and curr.next:
            # if you must delete last node, need to update tail pointer
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)