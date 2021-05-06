def majorityNum(nums, k):

    if not nums:
        return nums

    numsLen = len(nums)
    result = []
    required = numsLen//k
    hashMap = dict()

    for num in nums:
        hashMap[num] = hashMap.get(num, 0) +1

    for key, val in hashMap.items():
        if val > required:
            result.append(key)

    return result
print(majorityNum([1,2,2,3,4,5], 3))
print(majorityNum([2,1,2,0,3,2,3,2], 3))

