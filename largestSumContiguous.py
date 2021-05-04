class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        if not a:
            return 0
        if size == 1:
            return a
        cur_sum = 0
        max_sum = float("-inf")
        
        for num in a:
            cur_sum = max(cur_sum+num, num)
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
