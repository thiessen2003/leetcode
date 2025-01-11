def sliding_window(self, nums, k):
    if len(nums) < k: 
        return 0
    total = sum(nums[:k])
    maxTotal = total
    for i in range(len(nums)-k):
        total -= nums[i]
        total += nums[i+k]
        maxTotal = max(maxTotal, total)
    return maxTotal
