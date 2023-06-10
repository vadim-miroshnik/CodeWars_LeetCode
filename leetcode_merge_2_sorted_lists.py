# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# https://leetcode.com/problems/merge-two-sorted-lists/
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
    def mergeTwoLists1(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """ my version"""
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        node1 = list1
        node2 = list2
        res_head, res = None, None
        proc = True
        while proc:
            if node1.val < node2.val:
                if res is not None:
                    res.next = node1
                res = node1
                node_next = node1.next
                node1.next = None 
                node1 = node_next
            else:
                if res is not None:
                    res.next = node2
                res = node2
                node_next = node2.next
                node2.next = None
                node2 = node_next
            if res_head is None:
                res_head = res
            if node1 is None:
                res.next = node2
                break
            if node2 is None:
                res.next = node1
                break
        return res_head

    def mergeTwoLists2(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """Neetcode version"""
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


sol = Solution()
link_list1 = LinkedList([1, 2, 4])
link_list2 = LinkedList([1, 3, 4])
res = sol.mergeTwoLists2(link_list1.head, link_list2.head)
print_linked_list(res)
