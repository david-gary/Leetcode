# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        start = ListNode()
        out_list = start
        while list1 and list2:
            if list1.val < list2.val:
                out_list.next = list1
                list1 = list1.next
            else:
                out_list.next = list2
                list2 = list2.next
            out_list = out_list.next

        if list1:
            out_list.next = list1

        elif list2:
            out_list.next = list2

        return start.next
