def hasCycle(head):
    visited = set()
    if head is None:
        return None
    while head.next:
        visited.add(head)
        next_node = head.next
        if next_node in visited:
            return next_node
        else:
            head = head.next
    return None