# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# https://leetcode.com/problems/binary-tree-inorder-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None
        node = TreeNode(items[index])
        node.left = inner(index + 1)
        node.right = inner(index + 2)
        return node

    return inner()


class Solution:
    def inorderTraversal1(self, root: TreeNode | None) -> list[int]:
        """my first solution - recursive"""
        res = []
        if root:
            res = self.inorderTraversal1(root.left)
            res.append(root.val)
            res.extend(self.inorderTraversal1(root.right))
        return res

    def inorderTraversal2(self, root: TreeNode | None) -> list[int]:
        """Neetcode solution - iterative"""
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)  # начинаем вывод, когда дошли до левого края
            cur = cur.right
        return res


sol = Solution()
bt = to_binary_tree([1, None, 2, 3])
print(sol.inorderTraversal1(bt))
