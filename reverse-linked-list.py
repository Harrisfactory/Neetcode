# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        prv = None
        while head:
            nxt = head.next
            head.next = prv
            prv = head
            head = nxt
        return prv
