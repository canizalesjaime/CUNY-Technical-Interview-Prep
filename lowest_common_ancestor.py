# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# time complexity: O(n)
def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca or right_lca


def lowestCommonAncestorBST(root, p, q):
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left

        elif root.val < p.val and root.val < q.val:
            root = root.right

        else:
            return root      
