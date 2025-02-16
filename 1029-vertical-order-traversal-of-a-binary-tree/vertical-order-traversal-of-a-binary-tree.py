# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        
        queue = collections.deque()
        minCol, maxCol = float("inf"), float("-inf")

        queue.append((root, 0, 0))
        result = []
        colMap = collections.defaultdict(list)

        while queue:
            for _ in range(len(queue)):
                node, row, col = queue.popleft()

                colMap[col].append((row, node.val))

                minCol = min(minCol, col)
                maxCol = max(maxCol, col)

                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                
                if node.right:
                    queue.append((node.right, row + 1, col + 1))

                
        for i in range(minCol, maxCol + 1):
            colNodes = colMap[i]

            colNodes.sort(key = lambda x: (x[0], x[1]))

            result.append([val for row, val in colNodes])
        
        return result

