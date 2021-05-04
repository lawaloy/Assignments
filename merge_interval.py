class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals
        intervals.sort(key = lambda start: (start[0]))
        stack = []
        for idx, (startInt, endInt) in enumerate(intervals):
            if not stack or stack[-1][1] < startInt:
                stack.append([startInt, endInt])
            else:
                stack[-1][1] = max(stack[-1][1], endInt)
                
        return stack
