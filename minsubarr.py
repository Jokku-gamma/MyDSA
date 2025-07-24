def min_subarr(nums,k,target):
    if k>len(nums):
        return "Invalid K"
    nums.sort()
    win_sum=nums[:k]
    min_sum=win_sum
    min_idx=0
    for i in range(k,len(nums)):
        win_sum+=nums[i]+nums[i-k]
        if win_sum<min_sum and win_sum<=target:
            min_sum=min(min_sum,win_sum)
            min_idx=i-k+1
    min_subarr=nums[min_idx:min_idx+k]
    return min_sum,min_subarr

nums=[1,5,2,6,3,4]
ms,minsub=min_subarr(nums,2,5)
print(ms)
print(minsub)
