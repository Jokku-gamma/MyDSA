def subsets(arr):
    res=[]
    def backtrack(index,curr):
        res.append(list(curr))
        for i in range(index,len(arr)):
            curr.append(arr[i])
            backtrack(i+1,curr)
            curr.pop()
    backtrack(0,[])
    res.sort(key=lambda s:(len(s),s))
    return res

arr=[1,4,7,2]
print(subsets(arr))