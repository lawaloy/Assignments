class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):

        
        arr1_idx, arr2_idx, arr1Last = 0, 0, n-1
        
        while arr1_idx <= arr1Last and arr2_idx < m:
            if arr1[arr1_idx] > arr2[arr2_idx]:
                arr1[arr1Last], arr2[arr2_idx] = arr2[arr2_idx], arr1[arr1Last]
                arr1Last -= 1
                arr2_idx += 1
            else:
                arr1_idx += 1
