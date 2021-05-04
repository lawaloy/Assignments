class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        singleNum = 0
        for num in nums:
            singleNum ^= num
            
        return singleNum
