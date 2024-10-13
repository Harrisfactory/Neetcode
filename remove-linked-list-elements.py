# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        

        if not head:
            return None
        cur = head
        prev = cur

        #check/cycle as long as our first node is the target
        while head and head.val == val:
            head = head.next

        #cycle through list 
        while cur and cur.next:
            #while cur.next is our target, keep going
            while cur.next and cur.next.next and cur.next.val == val:
                cur.next = cur.next.next

            #move current
            prev = cur
            cur = cur.next
        
        #at end, check if our tail is the target
        if cur and cur.val == val:
            prev.next = None
        return head
    
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    solution = Solution()
    

    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(6)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    #ll: 1->2->6->3->4->5->7
    
    print('before')
    solution.printList(l1)
    s1 = solution.removeElements(l1, 6)
    print('after')
    solution.printList(s1)
    
