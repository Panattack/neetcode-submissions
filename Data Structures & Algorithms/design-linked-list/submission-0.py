class ListNode:
    def __init__(self, val: int = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size - 1 < index:
            return -1
        
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        cur = self.head
        self.head = ListNode(val)
        self.head.next = cur

    def addAtTail(self, val: int) -> None:
        self.size += 1
        cur = self.head

        while cur.next:
            cur = cur.next
        newNode = ListNode(val)
        cur.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        self.size += 1
        cur = self.head
        while index - 1 > 0:
            cur = cur.next
            index -= 1
        
        newNode = ListNode(val)
        nextNode = cur.next
        cur.next = newNode
        newNode.next = nextNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
                
        self.size -= 1
        cur = self.head

        while index - 1 > 0:
            cur = cur.next
            index -= 1

        cur.next = cur.next.next
    
    def printList(self):
        cur = self.head
        for _ in range(self.size):
            print(cur.val)
            cur = cur.next
        print("+++++++++++++")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)