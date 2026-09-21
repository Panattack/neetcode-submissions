# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []

        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        max_twin_sum = 0
        while stack:
            max_twin_sum = max(max_twin_sum, stack.pop() + slow.val)
            slow = slow.next

        return max_twin_sum