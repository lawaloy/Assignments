class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if not x and not y:
            return 0
        
        newNum = x ^ y
        
        check = 1
        count = 0
        while check <= newNum:
            
            if newNum & check:
                count += 1
            check = check << 1
        return count
