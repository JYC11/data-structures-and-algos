"""
         1
     2        3
  4   5    6      7
8 9 10 11 12 13 14 15

1,2,3,7,6,5,4,8,9,10,11,12

"""

from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


def print_zig_zag(node: TreeNode):
    queue = deque([node])
    values_per_level: dict[int, list[int]] = defaultdict(lambda: [])
    level = 1
    while queue:
        curr_node = queue.popleft()
        values_per_level[level].append(curr_node.val)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
        level += 1

    answer = ""

    for key, value in values_per_level.items():
        if key // 2 != 0:
            value.reverse()
            for val in value:
                answer += f"{str(val)},"
        else:
            for val in value:
                answer += f"{str(val)},"

    print(answer)
