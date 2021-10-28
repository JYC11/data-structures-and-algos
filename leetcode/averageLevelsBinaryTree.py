from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = deque()
        q.append(root)
        while q:
            summed = 0
            count = 0
            temp = deque()
            while q:
                n = q.popleft()
                summed += n.val
                count += 1
                if n.left != None:
                    temp.append(n.left)
                if n.right != None:
                    temp.append(n.right)
            q = temp
            result.append(summed*1.0/count)

        return result