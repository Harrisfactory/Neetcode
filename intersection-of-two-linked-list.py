# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

        lAHash = set()

        cur = headA
        while cur:
            lAHash.add(cur)
            cur = cur.next
        
        cur = headB
        while cur:
            if cur in lAHash:
                return cur
            cur = cur.next