# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        target = self.getLengthOfLL(head) - (n)

        #if target is at the front of the list
        if target == 0:
            return head.next

        #we want to move to right before n 
        cur = head
        ctr = 0
        while ctr < target - 1:
            cur = cur.next
            ctr+=1
        #then point to right after the target, if there is one
        if cur.next is None:
            return None
        elif cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        return head
        

    def getLengthOfLL(self, head) -> int:
        ctr = 0
        while head is not None:
            ctr+=1
            head = head.next
        return ctr
