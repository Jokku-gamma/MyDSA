def permute(nums):
    res=[]
    n=len(nums)
    visited=[False]*n
    def backtrack(curr):
        if len(curr)==n:
            res.append(list(curr))
            return 
        for i in range(n):
            if not visited[i]:
                curr.append(nums[i])
                visited[i]=True
                backtrack(curr)
                curr.pop()
                visited[i]=False
    backtrack([])
    return res

nums=[1,2]
print(permute(nums))