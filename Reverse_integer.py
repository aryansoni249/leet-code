class Solution:
    def reverse(self, x: int) -> int:
        hi=(2**31)-1
        low=(-2)**31
        t=str(x)
        
            
        t=t[::-1]
        if t[-1]=="-":
            t="-"+t[:-1]
            x=int(t)
        else:    
            x=int(t)
        if x>=low and x<=hi:
            return x
        else:
            return 0