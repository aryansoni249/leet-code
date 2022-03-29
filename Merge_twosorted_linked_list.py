#$ Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        one=list1
        two=list2
        head=ListNode()
        temp=head
        if one==None and two==None:
            return
        while one and  two:
            if one.val<two.val:
                temp.val=one.val
                one=one.next
                temp.next=ListNode()
                temp=temp.next
                
            elif one.val>two.val:
                temp.val=two.val
                two=two.next
                temp.next=ListNode()
                temp=temp.next                
            else:
                temp.val=one.val
                temp.next=ListNode(two.val)
                one=one.next
                two=two.next
                temp.next.next=ListNode()
                temp=temp.next.next
                
        if (one==None) and two!=None:
            
            while two:
                temp.val=two.val
                two=two.next
                temp.next=ListNode()
                temp=temp.next
        if two==None and one!=None:
            
            while one:
                temp.val=one.val
                one=one.next
                temp.next=ListNode()
                temp=temp.next
        temp=head
        prev=head
        while temp.next:
                prev=temp
                temp=temp.next
        prev.next=None 
          
        return head        