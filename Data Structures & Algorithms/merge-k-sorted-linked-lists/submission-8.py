# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        continuousList = list()
        for node in lists:
            while node:
                continuousList.append(node.val)
                node = node.next
        
        if not continuousList:
            return

        heapq.heapify(continuousList)

        prev = ListNode()
        head = prev

        while continuousList:
            curr = ListNode(heapq.heappop(continuousList))
            prev.next = curr
            prev = curr
        return head.next
