"""
         1
     2        3
  4   5    6      7
8 9 10 11 12 13 14 15

1,2,3,7,6,5,4,8,9,10,11,12

"""

from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


def print_zig_zag(node: TreeNode):
    queue = deque([(node, 1)])
    values_per_level: dict[int, list[int]] = defaultdict(lambda: [])
    while queue:
        curr_node, level = queue.popleft()
        values_per_level[level].append(curr_node.val)
        if curr_node.left:
            queue.append((curr_node.left, level + 1))
        if curr_node.right:
            queue.append((curr_node.right, level + 1))

    answer = ""

    for key, value in values_per_level.items():
        if key % 2 != 0:
            value.reverse()
            for val in value:
                answer += f"{str(val)},"
        else:
            for val in value:
                answer += f"{str(val)},"

    print(answer)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

print_zig_zag(root)
