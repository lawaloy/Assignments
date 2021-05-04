class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        
        def reverseNums(left, right):
            
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        numsLen = len(nums)-1
        lastBigIdx = len(nums)-1
        while lastBigIdx > 0 and nums[lastBigIdx] <= nums[lastBigIdx-1]:
            lastBigIdx -= 1
        
        if lastBigIdx != 0:
            check = None
            for idx in range(lastBigIdx, numsLen+1):
                if nums[idx] > nums[lastBigIdx-1]:
                    check = idx

            nums[check], nums[lastBigIdx-1] = nums[lastBigIdx-1], nums[check]
            reverseNums(lastBigIdx, numsLen)
            return nums
        
        reverseNums(0, numsLen)
        return nums
