# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergesorted(self, a,b):
        if a==None:
            return b
        if b==None:
            return a
        if a.val<b.val:
            result=a
            result.next=self.mergesorted(a.next,b)
        else:
            result=b
            result.next=self.mergesorted(a,b.next)
        return result    
    def middle(self,head):
        slow=head
        fast=head.next.next
        while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
        mid=slow.next
        slow.next=None
        return mid
        
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        m=self.middle(head)
        left=self.sortList(head)  
        right=self.sortList(m)
        r=self.mergesorted(left,right)
        return r
        
                    
            
            
        