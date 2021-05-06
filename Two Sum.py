class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) < 2:
            return []
        nums_map = dict()
        for idx in range(len(nums)):
            cur_num = nums[idx]
            diff = target - cur_num
            if cur_num in nums_map:
                return [nums_map[cur_num], idx]
            nums_map[diff] = idx
            
        return []
