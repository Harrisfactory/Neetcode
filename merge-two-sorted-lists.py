# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        elif not list2:
            return list1

        l3head = list3 = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                #process list1s current value
                list3.val = list1.val
                #move list1 over after processing current pointer
                list1 = list1.next
            else:
                #process list2s current value
                list3.val = list2.val
                #move list2 pointer over after processing current pointer
                list2 = list2.next
            #move list3s pointer over to a new node
            if list1 and list2:
                list3.next = ListNode()
                list3 = list3.next
        #atleast one list is empty, process other list
        if list1 or list2:
            if list1:
                list3.next = list1
            else:
                list3.next = list2
        
        return l3head
