# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelMap = defaultdict(list)
        res = []
        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                levelMap[level].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        for k, v in levelMap.items():
            res.append(v)

        return res

        