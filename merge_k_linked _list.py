class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list(ListNode)) -> ListNode():
        new=list()
        n=len(lists)
        if n==0 :
            
            return None
        if n==1:
            return lists[0]
        else:
            for i in lists:
                
                temp=i
                if i==None:
                    continue
                else:    
                    while temp:
                            new.append(temp.val)
                            temp=temp.next
            if len(new)==0:
                return
            new.sort()            
            optional=ListNode(new[0])
            temp=optional
            for i in new[1:]:
                temp.next=ListNode(i)
                temp=temp.next
            return optional    
            