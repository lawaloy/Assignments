class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums and not k:
            return 0
        if not nums:
            return 0
        
        def partitionArray(left, right, checkIdx):
            
            pivotValue = nums[checkIdx]
            nums[right], nums[checkIdx] = nums[checkIdx], nums[right]
            pivot = left
            
            for idx in range(left, right):
                if nums[idx] < pivotValue:
                    nums[idx], nums[pivot] = nums[pivot], nums[idx]
                    pivot += 1
                    
            nums[pivot], nums[right] = nums[right], nums[pivot]
            return pivot
        
        def q_select(left, right, kthLargest):
            
            if left > right:
                return 
            
            if left == right:
                return nums[left]
            
            pivotIdx = random.randint(left, right)
            
            pivotIdx = partitionArray(left, right, pivotIdx)
            
            if kthLargest == pivotIdx:
                return nums[pivotIdx]
            elif kthLargest > pivotIdx:
                return q_select(pivotIdx+1, right, kthLargest)
            else:
                return q_select(left, pivotIdx-1, kthLargest)
            
        
        kthLargest = len(nums) - k
        return q_select(0, len(nums)-1, kthLargest)
            
