def max_subarr(nums,k,target):
    if k>len(nums):
        return 0,[]
    nums.sort()
    win_sum=sum(nums[:k])
    if win_sum==target:
        return win_sum,nums[:k]
    max_sum=win_sum
    max_sub_ind=0
    for i in range(k,len(nums)):
        win_sum+=nums[i]-nums[i-k]
        if win_sum>max_sum and win_sum>=target:
            max_sum=win_sum
            max_sub_ind=i-k+1
    max_subarr=nums[max_sub_ind:max_sub_ind+k]
    return max_sum,max_subarr

nums=[1,5,2,6,3]
max_s,max_arr=max_subarr(nums,3,10)
print(f"Max sum: {max_s}, Subarray: {max_arr}")