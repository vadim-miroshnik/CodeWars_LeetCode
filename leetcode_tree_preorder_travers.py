# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]
# https://leetcode.com/problems/binary-tree-preorder-traversal/
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
        if index >= n or items[index] is None:
            return None
        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


# Function to insert nodes in level order
def insertLevelOrder(items, i=0):
    n = len(items)
    root = None
    if i < n:
        root = TreeNode(items[i])
        root.left = insertLevelOrder(items, 2 * i + 1)
        root.right = insertLevelOrder(items, 2 * i + 2)
    return root


class Solution:
    def preorderTraversal1(self, root: TreeNode | None) -> list[int]:
        """my first solution - recursive"""
        res = []
        if root:
            res.append(root.val)
            res.extend(self.preorderTraversal1(root.left))
            res.extend(self.preorderTraversal1(root.right))
        return res

    def preorderTraversal2(self, root: TreeNode | None) -> list[int]:
        """solution with generators"""

        def rec(node):
            if node is None:
                return
            yield node.val
            yield from rec(node.left)
            yield from rec(node.right)

        return list(rec(root))

    def preorderTraversal3(self, root: TreeNode | None) -> list[int]:
        """Iterative solution"""
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)  # начинаем вывод с вершин
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res


sol = Solution()
bt = to_binary_tree([1, None, 2, 3])
print(sol.preorderTraversal1(bt))
print(sol.preorderTraversal2(bt))

bt = to_binary_tree([3, 1, 2])
print(sol.preorderTraversal1(bt))
print(sol.preorderTraversal2(bt))  # Expected [3,1,2]

bt = to_binary_tree([3, 1, 2, 4, 5, 6])
print(sol.preorderTraversal1(bt))
print(sol.preorderTraversal2(bt))  # Expected [3, 1, 4, 5, 2, 6]
print(sol.preorderTraversal3(bt))  # Expected [3, 1, 4, 5, 2, 6]
