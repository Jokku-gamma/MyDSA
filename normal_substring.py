def substrings(s):
    res=[]
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            res.append(s[i:j+1])
    res.sort(key=lambda x:(len(x),x))
    return res

s="abc"
print(substrings(s))