from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next: Optional["TreeNode"] = None
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: Optional["ListNode"] = None
