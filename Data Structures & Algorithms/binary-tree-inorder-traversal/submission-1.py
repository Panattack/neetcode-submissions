# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ints = []

        def internal(root):
            if not root:
                return None

            internal(root.left)
            ints.append(root.val)
            internal(root.right)        
        
        internal(root)

        return ints