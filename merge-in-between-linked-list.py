# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        cur1 = list1
        ctr = 0
        list1 = cur1

        #march up to end of list1a
        while cur1 and ctr < a - 1:
            cur1 = cur1.next
            ctr+=1

        #save new head
        cur1mid = cur1

        #cut off mid segment of list1a
        while cur1 and ctr <= b:
            cur1 = cur1.next
            ctr+=1

        #place mid
        while cur1mid and list2:
            cur1mid.next = list2
            cur1mid = cur1mid.next
            list2 = list2.next

        cur1mid.next = cur1
        
        return list1