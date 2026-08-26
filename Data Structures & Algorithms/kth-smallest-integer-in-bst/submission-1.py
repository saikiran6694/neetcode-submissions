# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(curr):
            if not curr:
                return []

            return inorder_traversal(curr.left) + [curr.val] + inorder_traversal(curr.right)

        return inorder_traversal(root)[k-1] if k <= len(inorder_traversal(root)) else -1