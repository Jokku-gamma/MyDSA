def find_subarr(nums,target):
    prefix_sum={0:[-1]}
    csum=0
    res_arrs=[]
    for i in range(len(nums)):
        csum+=nums[i]
        compl=csum-target
        if compl in prefix_sum:
            for start in prefix_sum[compl]:
                subarr=nums[start+1:i+1]
                res_arrs.append(subarr)
        prefix_sum.setdefault(csum,[].append)
    return res_arrs

nums=[1,4,7,2,4,8,3]
print(find_subarr(nums,6))
