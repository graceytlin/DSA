# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    if not root:
        return None

    left = root.left
    root.left = root.right
    root.right = left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


