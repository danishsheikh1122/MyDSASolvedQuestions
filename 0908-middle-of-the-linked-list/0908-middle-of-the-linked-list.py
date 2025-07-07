# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # print(slow.next)
        # print(slow.next.next)
        return slow
        # return head      # returns full list
        # return head.next # returns list starting from 2nd node
        # return head.next.next # returns list starting from 3rd node
