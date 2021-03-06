def countingBits(num):
    ans = [0] * (num+1)
    for i in range (1, num+1):
        ans[i] = ans[i>>1] + (i&1)
    return ans
