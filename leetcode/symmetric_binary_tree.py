# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root):
    if root == None:
        return True
    def checkSymmetry(left, right):
        if not left and not right:
            return True
        elif left and right:
            return  left.val == right.val and \
            checkSymmetry(left.right, right.left) and \
            checkSymmetry(left.left, right.right)
        else:
            return False
    return checkSymmetry(root.left, root.right)

        