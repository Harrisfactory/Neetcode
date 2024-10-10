# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #I will use tortous and hair to append the first half of the ll
        
        #then as I traverse the 2nd half I just compare it with the list of reversed first half

        #this solution should be O(n) ish

        slowPtr = head
        fastPtr = head
        half = []

        def getlen(head):
            cur = head
            ctr = 0
            while cur:
                ctr+=1
                cur=cur.next
            return ctr

        llLen = getlen(head)

        while slowPtr and fastPtr and fastPtr.next:
            half.append(slowPtr.val)
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        #now at halfway point
        if llLen % 2 != 0:
            half.append(slowPtr.val)

        ctr = len(half) - 1

        while ctr >= 0 and slowPtr:
            if slowPtr.val != half[ctr]:
                return False
            slowPtr = slowPtr.next
            ctr-=1
        
        return True
