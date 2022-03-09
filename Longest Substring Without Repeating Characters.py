class Solution:
    def lengthOfLongestSubstring(self, s: str):
        new=list()
        ma_x=0
        for i in s:
            if i not in new:
                new.append(i)
            else:
                while i in new :
                    new.pop(0)
                new.append(i)
                
            l=len(new)
            ma_x=max(l,ma_x)
        return ma_x  
                
                
        
        