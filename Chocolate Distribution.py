class Solution:

    def findMinDiff(self, A,N,M):
        if not A:
            return 0
        if N < M:
            return 0
        
        min_chocolate = float("inf")
        A.sort()
        if N == M:
            return A[-1] - A[0]
          
        for idx in range(N-M+1):
            current_diff = A[idx+M-1] - A[idx]
            if current_diff < min_chocolate:
                min_chocolate = current_diff
                
        return min_chocolate
        
