# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node, then delete
        # 2 options
        # 0 - 1 children, return opposite child
        # 2 children, set val to min of right subtree, then delete that min node

        if not root:
            return None

        # find node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 0 - 1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # 2 children
            # find min of right child-subtree
            minNode = self.searchMinNode(root.right)
            # attach the left subtree of the deleted node as the left child of this successor
            res = root.right
            minNode.left = root.left
            del root
            # we return the right subtree as the replacement
            return res

        return root

    def searchMinNode(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur    