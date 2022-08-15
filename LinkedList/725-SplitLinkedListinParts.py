# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head, k: int):
        out_list = []

        # Find out the total length of the list
        curr, len_list = head, 0
        while curr:
            len_list += 1
            curr = curr.next

        sub_length = len_list//k
        leftover = len_list % k

        node, prev = head, None
        for i in range(k):
            out_list.append(node)
            for j in range(sub_length):
                if node:
                    prev = node
                    node = node.next
            if leftover and node:
                prev = node
                node = node.next
            if prev:
                prev.next = None
        return out_list
