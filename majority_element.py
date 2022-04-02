class Solution:
    def majorityElement(self, nums: list()) -> int:
        hashtable=dict()
        n=0
        for i in nums:
            if i in hashtable.keys():
                hashtable[i]+=1
                n+=1
            else:
                hashtable[i]=1
                n+=1
        for key in hashtable.keys():
            if hashtable[key]>int(n/2):
                return key
            else:
                continue