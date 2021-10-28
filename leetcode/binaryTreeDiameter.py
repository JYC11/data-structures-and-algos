class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]
        
        def dfs(root):
            if root is None:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            height = max(left,right) + 1
            max_diameter[0] = max(max_diameter[0],left + right + 2)

            return height
        dfs(root)
        return max_diameter[0]