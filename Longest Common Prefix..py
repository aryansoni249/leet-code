class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort()
        first=strs[0]
        ret=""
        boll=True
        for i in range(0,len(first)):
                for j in strs[1:]:
                    if first[i]==j[i]:
                        boll=True
                    else:
                        return ret
                if boll:
                    ret=ret+first[i]
        return ret
#strs=list of strings        