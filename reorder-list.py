# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #first were going to do floyds to obtain the middle of the LL
        slow_p = head
        fast_p = head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        second = slow_p.next
        #split the lists up
        slow_p.next = None
        #then we will reverse the 2nd LL
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #merge: then we just alternate while 2nd LL still exists then if any left in first LL append the rest

        #second will always be smaller so merge until second is empty
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
