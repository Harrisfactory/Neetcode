# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen_elems = set()

        cur = head
        while cur:
            if cur in seen_elems:
                return True
            seen_elems.add(cur)
            cur = cur.next

        return False
