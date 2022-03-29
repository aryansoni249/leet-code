class Solution:
    def isValid(self, s: str) -> bool:
        openb=['(','[','{']
        close=[')',']','}']
        new=list(s)
        stack=list()
        n=(len(s))
        if  n==1:
            return 0
        for i in s:
            if i in openb:
                 stack.append(i)
            else:
                if len(stack)!=0:
                    
                    if  openb.index(stack[-1])!=close.index(i):
                    
                        return 0
                     
                    else:
    
                        stack.pop(-1)
                else:
                      return 0
        if len(stack)!=0:
            return 0
        else:
             return 1