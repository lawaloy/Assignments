class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        cumSum = 0
        leftMax, rightMax = height[0], height[-1]
        leftSide, rightSide = 0, len(height)-1
        
        while leftSide <= rightSide:
            if leftMax < rightMax:
                if height[leftSide] < leftMax:
                    cur_diff = leftMax - height[leftSide]
                    cumSum += cur_diff
                else:
                    leftMax = max(leftMax, height[leftSide])
                leftSide += 1
            else:
                if height[rightSide] < rightMax:
                    cur_diff = rightMax - height[rightSide]
                    cumSum += cur_diff
                else:
                    rightMax = max(rightMax, height[rightSide])
                rightSide -= 1
        return cumSum
