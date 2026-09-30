# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        queue: List[TreeNode] = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            level_ls = []
            length_level = len(queue)
            for i in range(length_level):
                node = queue.popleft()
                level_ls.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_ls)

        return res
