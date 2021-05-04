class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if not nums:
            return nums
        seen_once, seen_twice = 0, 0
        
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
            
        return seen_once
