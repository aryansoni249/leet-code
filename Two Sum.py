def twoSum(self, nums, target: int) :
        t=len(nums)
        for i in range(t):
            for j in range(i+1,t):
                if nums[i]+nums[j]==target:
                    return [i,j]
                else:
                    continue
 # nums =list()
 #target=int()