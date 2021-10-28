def hasCycle(head):
    visited = set()
    if head is None:
        return False
    while head.next:
        visited.add(head)
        next_node = head.next
        if next_node in visited:
            return True
        else:
            head = head.next
    return False