class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        if nums[0] > 0:
            return result
        for firstIdx in range(len(nums)-2):
            if firstIdx > 0 and nums[firstIdx] == nums[firstIdx-1]:
                continue
            secondIdx = firstIdx +1
            thirdIdx = len(nums)-1
            
            while secondIdx < thirdIdx:
                totalSum = nums[firstIdx] + nums[secondIdx] + nums[thirdIdx]
                if totalSum == 0:
                    firstNum, secNum, thirdNum = nums[firstIdx], nums[secondIdx], nums[thirdIdx]
                    result.append([firstNum, secNum, thirdNum])
                    while secondIdx+1 < thirdIdx and nums[secondIdx] == nums[secondIdx+1]:
                        secondIdx += 1
                    while thirdIdx-1 > secondIdx and nums[thirdIdx]  == nums[thirdIdx-1]:
                        thirdIdx -= 1
                    secondIdx += 1
                    thirdIdx -= 1
                elif totalSum < 0:
                    secondIdx += 1
                else:
                    thirdIdx -= 1
        return result
        
