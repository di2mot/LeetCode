'''
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        b = ListNode()
        n = b

        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        if l1:
            n.next = l1
        elif l2:
            n.next = l2
        b.next
        return b.next
        '''
        Runtime: 62 ms, faster than 5.67% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.2 MB, less than 86.02% of Python3 online submissions for Merge Two Sorted Lists.
        '''