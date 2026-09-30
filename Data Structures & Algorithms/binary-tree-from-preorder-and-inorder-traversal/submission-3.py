# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None

        # rootVal = preorder[0]
        # mid = inorder.index(rootVal)
        # root = TreeNode(rootVal)
        # root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        # root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        # return root

        indices = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None

            rootVal = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(preorder) - 1)
