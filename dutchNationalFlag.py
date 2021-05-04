class Solution:
    def sort012(self,nums,n):
        
        if not nums:
            return nums
        
        left, runner, right = 0, 0, len(nums)-1
        
        while runner <= right:
            
            if nums[runner] == 0:
                nums[runner], nums[left] = nums[left], nums[runner]
                left += 1
                runner += 1
            elif nums[runner] == 2:
                nums[runner], nums[right] = nums[right], nums[runner]
                right -= 1
            else:
                runner += 1
        return nums
