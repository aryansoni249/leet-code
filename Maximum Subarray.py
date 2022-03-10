
class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            max_sum=0
            sum_till_now=0
            if max(nums)<0:
                return max(nums)
            else:
            
            
                
                for i in nums:
                    sum_till_now=sum_till_now+i
                    if sum_till_now>max_sum:
                        max_sum=sum_till_now
                    elif sum_till_now<0:
                         sum_till_now=0
                return max_sum
        
           
                
        