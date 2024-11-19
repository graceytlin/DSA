def lowest_common_ancestor(root, p, q):
    current = root

    while current:
        if root.val > p.val and root.val > q.val:
            current = root.right
        elif root.val < p.val and root.val < q.val:
            current = root.left
        else:
            return current

