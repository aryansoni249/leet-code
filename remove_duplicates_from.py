class Solution:
    def removeDuplicates(self, nums: list()) -> int:
        if len(nums)==1:
            return len(nums)
        for n in range(len(nums),0,-1):
            if n==1:
                return len(nums)
            if nums[n-1]==nums[n-2]:
                nums.pop(n-2)
        return len(nums)
            
        