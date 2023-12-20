# https://www.youtube.com/watch?v=KEcXDqthMLE&ab_channel=codestorywithMIK
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        if head.next == None:
            return
        
        fast, slow = head, head
        prevSlow = None
       
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        prevSlow.next = slow.next
        
        return head
