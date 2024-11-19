def hasCycle(head):
    visited = []
    current = head

    while current.next:
        if current.next in visited:
            return True
        else:
            visited.append(current)
            current = current.next

    return False

