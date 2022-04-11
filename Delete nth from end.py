class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head=ListNode(1)
head.next=ListNode(2)         
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=head
        if head.next==None and n==1:
            return
        l=0
        while temp:
            temp=temp.next
            l+=1
        k=l-n
        keep=head
        
        while k!=0:
            keep=keep.next
            k-=1
        keep.next=keep.next.next
        return head
o=Solution()
y=o.removeNthFromEnd(head,2)        
              