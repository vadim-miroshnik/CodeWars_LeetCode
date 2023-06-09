# # 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
# Note that the linked lists must retain their original structure after the function returns.
# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.
# If you correctly return the intersected node, then your solution will be accepted.
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
            # nodes.append(f"{node.val}({id(node)}))")
            nodes.append(f"{node.val}")
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """My first solution O(n*m)"""
        nodeA = headA
        while nodeA is not None:
            nodeB = headB
            while nodeB is not None:
                if nodeA is nodeB:
                    return nodeA
                nodeB = nodeB.next
            nodeA = nodeA.next
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """Neetcode solution - Two Pointers. Time O(n+m), Space O(1)"""
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        """Leetcode solution - Hashset. Time O(n+m), Space O(n)"""
        first_set = set()
        curr = headA
        while curr:
            first_set.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr = curr.next
        return None


def CustomJudge(intersectVal, listA: list, listB: list, skipA: int, skipB: int) -> bool:
    link_listA = LinkedList()
    int_node = None
    for i, elem in enumerate(listA):
        node = ListNode(elem)
        link_listA.add_last(node)
        if i == skipA:
            int_node = node
    print(link_listA)
    link_listB = LinkedList()
    for i, elem in enumerate(listB):
        node = ListNode(elem)
        link_listB.add_last(node)
        if i + 1 == skipB:
            node.next = int_node
            break
    print(link_listB)
    sol = Solution()
    res_node: ListNode = sol.getIntersectionNode2(link_listA.head, link_listB.head)
    if res_node:
        return res_node.val == intersectVal
    else:
        return 0 == intersectVal


print(CustomJudge(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3))
print(CustomJudge(2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1))
print(CustomJudge(0, [2, 6, 4], [1, 5], 3, 2))
