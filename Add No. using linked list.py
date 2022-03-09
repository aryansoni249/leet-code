class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1=ListNode(),l2= ListNode()) :
        one=str()
        cur=l1
        while cur:
            one += str(cur.val)
            cur=cur.next
        # print(one)
        one=int(one[::-1])
        cur2=l2
        two=str()
        while cur2:
            two+=str(cur2.val)
            cur2=cur2.next
        two=int(two[::-1])
        
        # print(two)
        three=one+two
        three=str(three)
        # print(three)
        li=list(three[::-1])
        
        head = ListNode(li[0])
        cur3 = ListNode(0)
        cur4 = ListNode(0)
        cur3 = head
        
        for i in li[1:]:
            temp = ListNode(i)
            cur4 =temp
            cur3.next = cur4
            cur3 = cur3.next
      
        return head