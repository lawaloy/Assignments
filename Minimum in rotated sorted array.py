  class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return []
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[-1] > nums[0]:
            return nums[0]
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = (low + high) >>1
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            #leftside sorted
            elif nums[mid] > nums[0]:
                low = mid
            else:
                high = mid-1
                
        return nums[low]
