# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assme the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1: Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        if lst:
            for elem in lst:
                node = ListNode(elem)
                self.add_last(node)

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"{node.val}")
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


def print_linked_list(node: ListNode):
    nodes = []
    while node is not None:
        nodes.append(f"{node.val}")
        node = node.next
    nodes.append("None")
    print("->".join(nodes))


class Solution:
    def addTwoNumbers1(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """my version"""
        dummy = ListNode()
        tail = dummy
        next_digit = 0

        while l1 or l2:
            tail.next = ListNode()
            tail = tail.next
            tail.val = next_digit
            tail.val += l1.val if l1 else 0
            tail.val += l2.val if l2 else 0
            if tail.val >= 10:
                next_digit = 1
                tail.val = tail.val - 10
            else:
                next_digit = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if next_digit > 0:
            tail.next = ListNode()
            tail = tail.next
            tail.val = next_digit
        return dummy.next

    def addTwoNumbers2(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """Neetcode version"""
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


sol = Solution()
link_list1 = LinkedList([2, 4, 3])
link_list2 = LinkedList([5, 6, 4])
res = sol.addTwoNumbers1(link_list1.head, link_list2.head)
print_linked_list(res)

link_list1 = LinkedList([9, 9, 9, 9, 9, 9, 9])
link_list2 = LinkedList([9, 9, 9, 9])
res = sol.addTwoNumbers1(link_list1.head, link_list2.head)
print_linked_list(res)
