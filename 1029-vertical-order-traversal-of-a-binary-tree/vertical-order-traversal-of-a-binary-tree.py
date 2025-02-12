# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnMap = collections.defaultdict(list)
        queue = deque()

        minColumn = float("inf")
        maxColumn = float("-inf")

        # Another func to go through hashmap list and swap places with the value that has the smaller value,
        # where they have the same coordinates
        queue.append((root, 0, 0))

        while queue:
            for i in range(len(queue)):
                node, row, col = queue.popleft()

                columnMap[col].append((node.val, row))

                minColumn = min(minColumn, col)
                maxColumn = max(maxColumn, col)

                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        
        res = []

        for i in range(minColumn, maxColumn + 1):
            if i in columnMap:
                items = columnMap[i]

                items.sort(key=lambda x: (x[1], x[0]))

                res.append([val for val, row in items])

        return res


