
def dfs(nums,index,dic,path,res):
    if index>=len(nums):
        res.append(path)
        return
    string1=dic[nums[index]]
    for i in string1:
        return dfs(nums,index+1,dic,path+i,res)


def telephone(nums):
    res=[]
    dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    if len(nums)==0:
        return res
    res=dfs(nums,0,dic,'',res)
    return res


print(telephone("467"))