class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if not nums:
            return nums
        
        occur = 1
        cand = nums[0]
        
        for num in nums[1:]:
            if num == cand:
                occur += 1
            else:
                occur -= 1
                if occur < 0:
                    occur = max(0, occur)
                    cand = num
        return cand
