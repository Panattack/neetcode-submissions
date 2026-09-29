# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True

        def postorder(root):
            nonlocal flag
            if not root:
                return 0

            # if not root.left and not root.right:
            #     return 1

            sum_left = postorder(root.left)
            sum_right = postorder(root.right)
            print(sum_left, sum_right, root.val)
            if abs(sum_left - sum_right) > 1:
                flag = False
            return max(sum_left, sum_right) + 1

        postorder(root)

        return flag 