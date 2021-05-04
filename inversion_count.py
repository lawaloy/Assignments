def inversion_count(arr, n):

      def merge(nums, num_arr, start, mid, end):

        left, right, runner, invCount = start, mid+1, start, 0

        while left <= mid and right <= end:

            if nums[left] < nums[right]:
                num_arr[runner] = (nums[left]
                left += 1
            else:
                num_arr[runner] = (nums[right])
                right += 1
                invCount += 1
            runner += 1

        while left <= mid:
            num_arr[runner] = nums[left]
            left += 1
            runner += 1

        while right <= end:
            num_arr[runner] = nums[right]
            right += 1
            runner += 1

        arr = num_arr[:]
        return invCount


    def _merge_sort(arr, temp_arr, left, right):

        invCount = 0

        if left < right:
            mid = left + (right-left)//2

            invCount += _merge_sort(arr, temp_arr, left, mid)
            invCount += _merge_sort(arr, temp_arr, mid+1, right)

            invCount += merge(arr, temp_arr, left, mid, right)
        return invCount

    def mergeSort(arr, n):
        
        temp_arr = [0] * n
        return _merge_sort(arr, temp, 0, n-1)

    return mergeSort(arr, n)
    

            
                               
