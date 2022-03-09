class Solution:
    def romanToInt(self, s: str) -> int:
        way={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return way[s[0]]
        else:
            s=s[::-1]
            store=way[s[0]]
            for i in range(1,len(s)):
                if (way[s[i-1]]<way[s[i]]) or (way[s[i-1]]==way[s[i]]) :
                    store=store+way[s[i]]
                else:
                    store=store-way[s[i]]
            return store