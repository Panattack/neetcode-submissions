# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        prev = None

        while curr:
            newNode = ListNode(curr.val, prev)
            prev = newNode
            curr = curr.next

        while head and prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next

        return True
